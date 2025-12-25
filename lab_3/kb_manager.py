import json
import os


class KBManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.knowledge = {}
        self.load_kb()

    def load_kb(self):
        with open(self.file_path, "r") as f:
            raw_data = json.load(f)

        for triple in raw_data:
            sub = triple["sub"]
            req = triple["rel"]
            obj = triple["obj"]

            if sub not in self.knowledge:
                self.knowledge[sub] = {}

            if req not in self.knowledge[sub]:
                self.knowledge[sub][req] = []

            self.knowledge[sub][req].append(obj)

    def get_node_relations(self, node):
        return self.knowledge.get(node.lower(), {})

    def look_up(self):
        # print(self._forward_index)
        print(self.knowledge)
        # print(self.get_node_relations("terminal"))
