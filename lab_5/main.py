import sys
from PySide6.QtWidgets import QApplication

from core.main_window import MainWindow
from core.data_manager import DataManager
from core.neural_network import NeuralNetwork

GRID_SIZE = 28
INPUT_NEURONS = GRID_SIZE * GRID_SIZE


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = DataManager(
        training_f="training_data.json", weight_f="weights.json", epochs_d="epochs"
    )
    network = NeuralNetwork(
        objects_set=["+", "-", "∞", "="], input_neurons_qnty=INPUT_NEURONS
    )
    window = MainWindow(data_manager=manager, neural_net=network, grid_size=GRID_SIZE)
    window.show()
    sys.exit(app.exec())
