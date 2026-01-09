import numpy as np


class NeuralNetwork:
    def __init__(
        self, objects_set, input_neurons_qnty, hidden_neurons_qnty=64, learning_rate=0.5
    ):
        self._objects_set = objects_set

        self._in_neurons = input_neurons_qnty
        self._hidden_neurons = hidden_neurons_qnty
        self._out_neurons = len(self._objects_set)

        self.learning_rate = learning_rate

        mean_value = 0.0
        xavier_std_deviation = lambda neurons: (np.pow(neurons, -0.5))
        self.in_hid_matrix = np.random.normal(
            loc=mean_value,
            scale=xavier_std_deviation(self._in_neurons),
            size=(self._hidden_neurons, self._in_neurons),
        )
        self.hid_out_matrix = np.random.normal(
            loc=0.0,
            scale=xavier_std_deviation(self._hidden_neurons),
            size=(self._out_neurons, self._hidden_neurons),
        )

    def get_objects_set(self):
        return self._objects_set

    def sigmoid_activation_func(self, x):
        return 1 / (1 + np.exp(-x))
