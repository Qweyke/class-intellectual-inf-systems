import sys
from PySide6.QtWidgets import QApplication
from main_window import ExpertSystemUI

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ExpertSystemUI()
    window.show()

    sys.exit(app.exec())
