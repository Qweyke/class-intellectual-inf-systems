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
    QInputDialog,
    QMessageBox,
    QTableWidgetItem,
)
from PySide6.QtGui import Qt
from data_handler import DataProvider
from models import DecisionCore


class ExpertSystemUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Collective decision-making system")
        self.resize(800, 600)

        self._arrange_init_widgets()
        self._do_init_connects()
        self._create_init_table()

        self._dp = DataProvider()

    def _arrange_init_widgets(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.controls_layout = QHBoxLayout()
        self.btn_choose_scenario = QPushButton("Choose ready-made scenario")
        self.btn_calculate = QPushButton("Evaluate the result")
        self.btn_calculate.setStyleSheet(
            "background-color: #4CAF50; color: white; font-weight: bold;"
        )

        self.controls_layout.addWidget(self.btn_choose_scenario)
        self.controls_layout.addStretch()
        self.controls_layout.addWidget(self.btn_calculate)

        self.layout.addLayout(self.controls_layout)
        self.layout.addWidget(QLabel("Provided data"))

    def _create_init_table(self):
        self.table = QTableWidget(0, 0)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        self.layout.addWidget(QLabel("Analysis results:"))
        self.results_output = QTextEdit()
        self.results_output.setReadOnly(True)
        self.layout.addWidget(self.results_output)

    def _do_init_connects(self):
        self.btn_choose_scenario.clicked.connect(self.provide_scenario)
        self.btn_calculate.clicked.connect(self.run_calculation)

    def _update_table(self):
        current_scenario = self._dp.get_current_scenario()
        if current_scenario is None:
            QMessageBox.warning(self, "Error", "Current scenario is empty")
            return

        self.table.setColumnCount(len(current_scenario.options))
        self.table.setRowCount(len(current_scenario.experts))
        self.table.setHorizontalHeaderLabels(current_scenario.options)
        self.table.setVerticalHeaderLabels(current_scenario.experts)

        for r, row_data in enumerate(self._dp.get_current_scenario().matrix):
            for c, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(r, c, item)

    def provide_scenario(self):
        scenarios = self._dp.get_scenario_names()

        s_name, ok = QInputDialog.getItem(
            self,
            "Ready-made scenarios",
            "Choose scenario:",
            scenarios,
            0,
            False,
        )
        if (not ok) or (s_name is None):
            QMessageBox.warning(self, "Error", "Bad scenario choice")
            return

        self.results_output.append(f"Chosen scenario: {s_name}\n")
        self._dp.set_current_scenario(s_name)
        self._update_table()

    def run_calculation(self):
        current_scenario = self._dp.get_current_scenario()
        if current_scenario is None:
            QMessageBox.warning(self, "Error", "No scenario chosen")
            return

        self.results_output.clear()

        core = DecisionCore(current_scenario)

        report = []
        report.append(f"=== ANALYZING SCENARIO: {current_scenario.name} ===\n")

        report.append("--- 1. PLURALITY MODEL ---")
        report.append(core.plurality_model())
        report.append("-" * 30 + "\n")

        report.append("--- 2. CONDORCET METHODS ---")
        report.append("[2.1 Clear Winner]")
        report.append(core.condorcet_clear_winner_rule())
        report.append("")

        report.append("[2.2 Copeland Rule]")
        report.append(core.condorcet_copeland_rule())
        report.append("")

        report.append("[2.3 Simpson (Minimax) Rule]")
        report.append(core.condorcet_simpson_rule())

        report.append("--- 3. BORDA COUNT MODEL ---")
        report.append(core.borda_model())
        report.append("-" * 30 + "\n")

        report.append("\n" + "=" * 40)

        full_text = "\n".join(report)
        self.results_output.append(full_text)
