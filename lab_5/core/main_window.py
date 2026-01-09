from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QFrame

from PySide6.QtGui import Qt

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

    def _do_init_connects(self):
        self._ui.clear_btn.clicked.connect(self._canvas.clear)
        self._ui.auto_check.checkStateChanged.connect(
            lambda: (
                self._ui.accept_btn.setEnabled(True)
                if self._ui.auto_check.isChecked()
                else self._ui.accept_btn.setDisabled(True)
            )
        )
        self._ui.accept_btn.clicked.connect(
            lambda: self._data_manager.save_object_sample(
                label=self._ui.obj_box.currentText(), vector=self._canvas.get_vector()
            )
        )

        # self._ui.determine_btn.clicked.connect(self.run_calculation)
