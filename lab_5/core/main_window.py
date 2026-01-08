from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QFrame

from PySide6.QtGui import Qt

from gui.mainwindow_ui import Ui_MainWindow
from core.drawing_canvas import DrawingCanvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._ui.canvas_frame.setFrameShape(QFrame.StyledPanel)
        self._ui.canvas_frame.setStyleSheet(
            "background-color: #f0f0f0; border: 2px solid #444;"
        )
        frame_layout = QVBoxLayout(self._ui.canvas_frame)
        frame_layout.setContentsMargins(0, 0, 0, 0)

        self._canvas = DrawingCanvas(parent=self._ui.canvas_frame)
        frame_layout.addWidget(self._canvas, alignment=Qt.AlignCenter)
        self.adjustSize()

        self._do_init_connects()

    def _do_init_connects(self):
        self._ui.clear_btn.clicked.connect(self._canvas.clear)
        # self._ui.determine_btn.clicked.connect(self.run_calculation)
