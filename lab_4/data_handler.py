import json
import os

import numpy as np


class Scenario:
    def __init__(self, name, options, experts, matrix):
        self.name = name
        self.options = options
        self.experts = experts
        self.matrix = np.array(matrix)


class DataProvider:
    def __init__(self, file_path="lab_4/samples.json"):
        self._file_path = file_path
        self._scenarios = []
        self.current_scenario = None
        self.load_data()

    def load_data(self):
        if not os.path.exists(self._file_path):
            print(f"No sample file exists on path {self._file_path}")
            return

        try:
            with open(self._file_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                for item in raw_data.get("scenarios", []):
                    if len(item["matrix"]) == len(item["experts"]):
                        scenario = Scenario(
                            item["name"],
                            item["options"],
                            item["experts"],
                            item["matrix"],
                        )
                        self._scenarios.append(scenario)
        except Exception as e:
            print(f"Can't read file: {e}")

    def _get_scenario_by_index(self, index):
        if 0 <= index < len(self._scenarios):
            return self._scenarios[index]
        return None

    def _get_scenario_by_name(self, name):
        for s in self._scenarios:
            if s.name == name:
                return s
        return None

    def get_scenario_names(self):
        return [s.name for s in self._scenarios]

    def set_current_scenario(self, name):
        self.current_scenario = self._get_scenario_by_name(name)

    def get_current_scenario(self):
        return self.current_scenario
