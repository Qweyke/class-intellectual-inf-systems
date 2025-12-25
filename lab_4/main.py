import sys
from PySide6.QtWidgets import QApplication, QInputDialog, QMessageBox
from data_handler import DataProvider
from main_window import ExpertSystemUI


class ExpertSystemApp(ExpertSystemUI):
    def __init__(self):
        super().__init__()

        self.btn_add_expert.clicked.connect(self.add_expert_dialog)
        self.btn_add_option.clicked.connect(self.add_option_dialog)
        self.btn_calculate.clicked.connect(self.run_calculation)

    def add_expert_dialog(self):
        name, ok = QInputDialog.getText(self, "Эксперт", "Введите имя эксперта:")
        if ok and name:
            self.experts.append(name)
            self.update_table()

    def add_option_dialog(self):
        name, ok = QInputDialog.getText(
            self, "Вариант", "Введите название альтернативы:"
        )
        if ok and name:
            self.options.append(name)
            self.update_table()

    def run_calculation(self):
        # Пока просто заглушка для проверки
        if not self.experts or not self.options:
            QMessageBox.warning(self, "Ошибка", "Добавьте экспертов и варианты!")
            return

        self.results_output.setText(
            "Логика расчетов будет подключена в следующем модуле..."
        )


if __name__ == "__main__":

    dp = DataProvider()
    # app = QApplication(sys.argv)

    # window = ExpertSystemApp()
    # window.show()

    # sys.exit(app.exec())
