from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QLabel,
    QHeaderView,
    QTextEdit,
)
from PySide6.QtCore import Qt


class ExpertSystemUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Система принятия коллективных решений")
        self.resize(800, 600)

        # Главный виджет и слой
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Панель управления (Кнопки добавления)
        self.controls_layout = QHBoxLayout()
        self.btn_add_expert = QPushButton("Добавить эксперта")
        self.btn_add_option = QPushButton("Добавить вариант")
        self.btn_calculate = QPushButton("Рассчитать результат")
        self.btn_calculate.setStyleSheet(
            "background-color: #4CAF50; color: white; font-weight: bold;"
        )

        self.controls_layout.addWidget(self.btn_add_expert)
        self.controls_layout.addWidget(self.btn_add_option)
        self.controls_layout.addStretch()
        self.controls_layout.addWidget(self.btn_calculate)

        self.layout.addLayout(self.controls_layout)

        # Инструкция
        self.layout.addWidget(
            QLabel("Заполните таблицу рангов (1 - лучший, N - худший):")
        )

        # Таблица данных
        self.table = QTableWidget(0, 0)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Зона вывода результатов
        self.layout.addWidget(QLabel("Результаты анализа:"))
        self.results_output = QTextEdit()
        self.results_output.setReadOnly(True)
        self.layout.addWidget(self.results_output)

        self.experts = []
        self.options = []

    def update_table(self):
        self.table.setColumnCount(len(self.options))
        self.table.setRowCount(len(self.experts))
        self.table.setHorizontalHeaderLabels(self.options)
        self.table.setVerticalHeaderLabels(self.experts)
