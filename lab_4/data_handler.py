import json
import os

import numpy as np


class Scenario:
    """Объект-контейнер для одного сценария выборки"""

    def __init__(self, name, candidates, experts, matrix):
        self.name = name
        self.candidates = candidates
        self.experts = experts
        self.matrix = np.array(matrix)


class DataProvider:
    def __init__(self, file_path="lab_4/samples.json"):
        self.file_path = file_path
        self.scenarios = []
        self.load_data()

    def load_data(self):
        """Парсинг JSON и создание объектов Scenario"""
        if not os.path.exists(self.file_path):
            print(f"No sample file exists on path {self.file_path}")
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                for item in raw_data.get("scenarios", []):
                    if len(item["matrix"]) == len(item["experts"]):
                        scene = Scenario(
                            item["name"],
                            item["candidates"],
                            item["experts"],
                            item["matrix"],
                        )
                        self.scenarios.append(scene)
        except Exception as e:
            print(f"Ошибка при чтении справочника: {e}")

    def get_scenario_names(self):
        """Возвращает список названий для выпадающего списка в GUI"""
        return [s.name for s in self.scenarios]

    def get_scenario_by_index(self, index):
        if 0 <= index < len(self.scenarios):
            return self.scenarios[index]
        return None
