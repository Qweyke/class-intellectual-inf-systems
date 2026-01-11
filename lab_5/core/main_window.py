import time
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QFrame, QApplication

from PySide6.QtGui import Qt
import numpy as np

from gui.mainwindow_ui import Ui_MainWindow
from core.drawing_canvas import DrawingCanvas
from core.neural_network import NeuralNetwork
from core.data_manager import DataManager


class MainWindow(QMainWindow):

    def __init__(self, data_manager: DataManager, neural_net: NeuralNetwork, grid_size):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.adjustSize()

        self._data_manager = data_manager
        self._neural_net = neural_net

        self._canvas = DrawingCanvas(parent=self._ui.canvas_frame, grid_size=grid_size)
        self._assemble_canvas_widget()

        self._fill_objects_combobox()
        self._do_init_connects()

        self.update_stats_display()

    def _assemble_canvas_widget(self):
        self._ui.canvas_frame.setFrameShape(QFrame.StyledPanel)
        self._ui.canvas_frame.setStyleSheet(
            "background-color: #f0f0f0; border: 2px solid #444;"
        )
        frame_layout = QVBoxLayout(self._ui.canvas_frame)
        frame_layout.setContentsMargins(0, 0, 0, 0)
        frame_layout.addWidget(self._canvas, alignment=Qt.AlignCenter)

    def _fill_objects_combobox(self):
        self._ui.obj_box.addItems(self._neural_net.get_objects_set())

    def _on_clear_clicked(self):
        self._canvas.clear()
        self._ui.res_label.setText("Result: None")

    def _save_and_clear(self):
        label = self._ui.obj_box.currentText()

        samples_pack = self._canvas.get_augmented_dataset(count=5)

        self._data_manager.save_object_sample_batch(label=label, vectors=samples_pack)

        self._on_clear_clicked()
        self.update_stats_display()

    def update_stats_display(self):
        stats = self._data_manager.get_dataset_statistics()
        if not stats:
            self._ui.statusBar.showMessage("Dataset is empty")
            return

        stat_strings = [f"'{label}': {count}" for label, count in stats.items()]
        full_text = "Samples: " + " | ".join(stat_strings)

        self._ui.statusBar.showMessage(full_text)

    def _on_determine_clicked(self):
        label, weights = self._neural_net.query(self._canvas.get_sample_vector())
        self._ui.res_label.setText(f"Result: {label}\nWeights: {weights}")

    def _do_init_connects(self):
        self._ui.clear_btn.clicked.connect(self._on_clear_clicked)
        self._ui.accept_btn.clicked.connect(self._save_and_clear)
        self._ui.teach_btn.clicked.connect(self.run_training)
        self._ui.determine_btn.clicked.connect(self._on_determine_clicked)

        self._ui.accuracy_btn.clicked.connect(
            lambda: self._ui.statusBar.showMessage(
                f"{self._neural_net.check_accuracy(
                    self._data_manager.load_samples_dataset()
                )}"
            )
        )

        self._ui.display_btn.clicked.connect(self.debug_view_database)

    def run_training(self):
        self._ui.statusBar.showMessage("Initiating learning...")

        self._neural_net.train_full_dataset()
        self._ui.statusBar.showMessage("Learning complete!")

    def debug_view_database(self, *args, batch_size=6):
        dataset = self._data_manager.load_samples_dataset()

        if not dataset:
            return

        all_samples = []
        for label, vectors in dataset.items():
            for v in vectors:
                all_samples.append((label, v))

        print(
            f"Training data size: {len(all_samples)} samples. Displaying each {batch_size}..."
        )

        for i in range(0, len(all_samples), batch_size):
            current_batch = all_samples[i : i + batch_size]

            print(f"\nBatch {i//batch_size + 1}:")

            for j, (label, vector) in enumerate(current_batch):
                matrix = np.array(vector).reshape(
                    self._canvas.grid_size, self._canvas.grid_size
                )

                self._canvas.grid = matrix.copy()
                self._canvas.update()

                QApplication.processEvents()

                print(f"Sample {i + j}: Object '{label}'")
                time.sleep(0.6)

            time.sleep(2.0)
