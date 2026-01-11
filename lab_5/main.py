import sys
import os
from PySide6.QtWidgets import QApplication

from core.main_window import MainWindow
from core.data_manager import DataManager
from core.neural_network import NeuralNetwork

GRID_SIZE = 28
INPUT_NEURONS = GRID_SIZE * GRID_SIZE
LAB_DIR = os.path.dirname(os.path.abspath(__file__))

object_dict = {
    "+": [0.99, 0.01, 0.01, 0.01],
    "√": [0.01, 0.99, 0.01, 0.01],
    "∞": [0.01, 0.01, 0.99, 0.01],
    "=": [0.01, 0.01, 0.01, 0.99],
}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = DataManager(
        training_f=os.path.join(LAB_DIR, "training_data"),
        weight_f=os.path.join(LAB_DIR, "weights"),
        epochs_d=os.path.join(LAB_DIR, "epochs"),
    )
    network = NeuralNetwork(
        data_manager=manager, objects_set=object_dict, input_neurons_qnty=INPUT_NEURONS
    )
    window = MainWindow(data_manager=manager, neural_net=network, grid_size=GRID_SIZE)
    window.show()
    sys.exit(app.exec())
