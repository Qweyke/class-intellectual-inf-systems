import json
import os
import numpy as np


class DataManager:
    def __init__(self, training_f: str, weight_f: str, epochs_d: str):
        self._training_filename = training_f + ".npz"
        self._weights_filename = weight_f + ".npz"
        self._epochs_dir = epochs_d

    def save_object_sample_batch(self, label: str, vectors: list):
        dataset = self.load_samples_dataset()

        new_vectors = np.array(vectors, dtype=np.float32)
        if label in dataset:
            dataset[label] = np.vstack([dataset[label], new_vectors])
        else:
            dataset[label] = new_vectors

        np.savez_compressed(self._training_filename, **dataset)

    def load_samples_dataset(self):
        if not os.path.exists(self._training_filename):
            return {}
        try:
            with np.load(self._training_filename) as data:
                return {label: data[label] for label in data.files}
        except Exception as e:
            print(f"Error loading dataset: {e}")
            return {}

    def get_dataset_statistics(self):
        dataset = self.load_samples_dataset()
        return {label: len(vectors) for label, vectors in dataset.items()}

    # Weights (Numpy Binary Format)
    def save_weights(self, in_hid_matrix, hid_out_matrix):
        # np.savez saves multiple arrays into a single compressed .npz file
        np.savez_compressed(
            self._weights_filename, w_in_hid=in_hid_matrix, w_hid_out=hid_out_matrix
        )
        print(f"Save weights: Success (Binary File '{self._weights_filename}')")

    def load_weights(self):
        if not os.path.exists(self._weights_filename):
            print(f"Load weights: Fail (File '{self._weights_filename}' not found)")
            return None, None
        try:
            data = np.load(self._weights_filename)
            print(f"Load weights: Success (File '{self._weights_filename}')")
            return data["w_in_hid"], data["w_hid_out"]
        except Exception as e:
            print(f"Error loading weights: {e}")
            return None, None

    # Snapshots (Numpy Binary Format)
    def save_snapshot(self, epoch, in_hid_matrix, hid_out_matrix):
        if not os.path.exists(self._epochs_dir):
            os.makedirs(self._epochs_dir)

        filename = os.path.join(self._epochs_dir, f"weights_epoch_{epoch}.npz")
        np.savez_compressed(
            filename, epoch=epoch, w_in_hid=in_hid_matrix, w_hid_out=hid_out_matrix
        )
        print(f"Save epoch snapshot: Success (Epoch '{epoch}')")

    def load_snapshot(self, epoch):
        filename = os.path.join(self._epochs_dir, f"weights_epoch_{epoch}.npz")
        if not os.path.exists(filename):
            print(f"Load weights: Fail (File for epoch '{epoch}' not found)")
            return None, None
        try:
            data = np.load(filename)
            print(f"Load weights from epoch: Success ('{epoch}')")
            return data["w_in_hid"], data["w_hid_out"]
        except Exception as e:
            print(f"Error loading snapshot: {e}")
            return None, None
