import json
import os
import numpy as np


class DataManager:
    def __init__(self, training_f, weight_f, epochs_d):
        self._training_filename = training_f
        self._weights_filename = weight_f
        self._epochs_dir = epochs_d

    def save_object_sample(self, label, vector):
        data = {}
        if os.path.exists(self._training_filename):
            with open(self._training_filename, "r") as f:
                data = json.load(f)

        if label not in data:
            data[label] = []
        data[label].append(vector)

        with open(self._training_filename, "w") as f:
            json.dump(data, f)

    def save_weights(
        self,
        in_hid_martix,
        hid_out_martix,
    ):
        data = {
            "w_in_hid": in_hid_martix.tolist(),
            "w_hid_out": hid_out_martix.tolist(),
        }
        with open(self._weights_filename, "w") as f:
            json.dump(data, f)
        print(f"Save weights: Success (File '{self._weights_filename}')")

    def load_weights(self):
        try:
            with open(self._weights_filename, "r") as f:
                data = json.load(f)

            w_in_hid = np.array(data["w_in_hid"])
            w_hid_out = np.array(data["w_hid_out"])
            print(f"Load weights: Success (File '{self._weights_filename}')")
            return w_in_hid, w_hid_out

        except FileNotFoundError:
            print(f"Load weights: Fail (File '{self._weights_filename}' not found)")
            return None, None

    def save_snapshot(self, epoch, in_hid_matrix, hid_out_matrix):
        if not os.path.exists(self._epochs_dir):
            os.makedirs(self._epochs_dir)

        filename = f"{self._epochs_dir}/weights_epoch_{epoch}.json"
        data = {
            "epoch": epoch,
            "w_in_hid": in_hid_matrix.tolist(),
            "w_hid_out": hid_out_matrix.tolist(),
        }

        with open(filename, "w") as f:
            json.dump(data, f)
        print(f"Save epoch snapshot: Success (Epoch '{epoch}')")

    def load_snapshot(self, epoch):
        filename = f"{self._epochs_dir}/weights_epoch_{epoch}.json"
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            w_in_hid = np.array(data["w_in_hid"])
            w_hid_out = np.array(data["w_hid_out"])

            print(f"Load weights from epoch: Success ('{epoch}')")
            return w_in_hid, w_hid_out

        except FileNotFoundError:
            print(f"Load weights: Fail (File for epoch '{epoch}' not found)")
            return None, None
