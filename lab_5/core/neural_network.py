import random
import numpy as np

from core.data_manager import DataManager


class NeuralNetwork:
    def __init__(
        self,
        data_manager: DataManager,
        objects_set: dict,
        input_neurons_qnty,
        hidden_neurons_qnty=64,
        learning_rate=0.5,
        epochs_qnty=300,
    ):
        self._data_manager = data_manager
        self._objects_set = objects_set

        self._in_neurons = input_neurons_qnty
        self._hidden_neurons = hidden_neurons_qnty
        self._out_neurons = len(self._objects_set)

        self._learning_rate = learning_rate
        self._epochs_qnty = epochs_qnty

        if not self._load_trained_model():
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

    def sigmoid_activation_func(self, X):
        return 1 / (1 + np.exp(-X))

    def get_objects_set(self):
        return self._objects_set.keys()

    def do_single_sample_training(self, target_name, current_inputs_vector, custom_lr):
        target_outputs = self._objects_set[target_name]

        inputs_vector = (np.array(current_inputs_vector, ndmin=2).T * 0.98) + 0.01

        hidden_inputs = np.dot(self.in_hid_matrix, inputs_vector)
        hidden_outputs = self.sigmoid_activation_func(hidden_inputs)

        final_inputs = np.dot(self.hid_out_matrix, hidden_outputs)
        final_outputs = self.sigmoid_activation_func(final_inputs)

        targets = np.array(target_outputs, ndmin=2).T

        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.hid_out_matrix.T, output_errors)

        out_grad = output_errors * final_outputs * (1.0 - final_outputs)
        hid_grad = hidden_errors * hidden_outputs * (1.0 - hidden_outputs)

        self.hid_out_matrix += custom_lr * np.dot(out_grad, hidden_outputs.T)
        self.in_hid_matrix += custom_lr * np.dot(hid_grad, inputs_vector.T)

    def _load_trained_model(self):
        self.in_hid_matrix, self.hid_out_matrix = self._data_manager.load_weights()

        if (self.in_hid_matrix is not None) and (self.hid_out_matrix is not None):
            return True

        return False

    def train_full_dataset(self, split_ratio=0.8, batch_size=16):
        dataset = self._data_manager.load_samples_dataset()
        all_samples = []
        for label, vectors in dataset.items():
            for v in vectors:
                all_samples.append((label, v))

        random.shuffle(all_samples)
        split_index = int(len(all_samples) * split_ratio)
        train_set = all_samples[:split_index]
        val_set = all_samples[split_index:]

        print(f"Standard Training | Train: {len(train_set)}, Val: {len(val_set)}")

        for epoch in range(1, self._epochs_qnty + 1):
            random.shuffle(train_set)

            # Разрезаем данные на батчи
            for i in range(0, len(train_set), batch_size):
                batch = train_set[i : i + batch_size]

                # Обучаем на батче (градиенты внутри do_single суммируются)
                for label, vector in batch:
                    # Используем стабильный LR без "встрясок"
                    self.do_single_sample_training(label, vector, self._learning_rate)

            if epoch % 10 == 0:
                acc = self.calculate_accuracy_on_set(val_set)
                print(f"Epoch {epoch:3} | Accuracy: {acc:.2f}%")

        self.print_confusion_matrix(val_set)
        self._data_manager.save_weights(self.in_hid_matrix, self.hid_out_matrix)

    def query(self, inputs_list):
        inputs = (np.array(inputs_list, ndmin=2).T * 0.98) + 0.01

        hidden_in = np.dot(self.in_hid_matrix, inputs)
        hidden_out = self.sigmoid_activation_func(hidden_in)

        final_in = np.dot(self.hid_out_matrix, hidden_out)
        final_out = self.sigmoid_activation_func(final_in)

        index_of_max = np.argmax(final_out)
        return (
            list(self._objects_set.keys())[index_of_max],
            final_out.flatten().tolist(),
        )

    def check_accuracy(self, dataset):
        correct = 0
        total = 0
        for label, vectors in dataset.items():
            for v in vectors:
                total += 1
                prediction_name, _ = self.query(v)
                if prediction_name == label:
                    correct += 1

        if total == 0:
            return 0.0

        accuracy = (correct / total) * 100
        return accuracy

    def calculate_accuracy_on_set(self, data_list):
        if not data_list:
            return 0.0

        correct = 0
        for label, v in data_list:
            prediction_name, _ = self.query(v)
            if prediction_name == label:
                correct += 1

        return (correct / len(data_list)) * 100

    def print_confusion_matrix(self, val_set):
        stats = {}
        for label, v in val_set:
            pred, _ = self.query(v)
            if label not in stats:
                stats[label] = {}
            stats[label][pred] = stats[label].get(pred, 0) + 1

        print("\nError Matrix:")
        for true_label, preds in stats.items():
            print(f"For '{true_label}' guessed: {preds}")
