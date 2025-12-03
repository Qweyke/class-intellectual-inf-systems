import json


class Fact:
    def __init__(self, predicate, args, source="initial"):
        self.predicate = predicate
        self.args = args
        self.source = source

    def __str__(self):
        return f"{self.predicate}({', '.join(map(str, self.args))})"

    def __repr__(self):
        return f"Fact({self.predicate}, {self.args}, source={self.source})"


class Rule:
    def __init__(self, name, lhs, rhs, priority=0):
        self.name = name
        self.lhs = lhs
        self.rhs = rhs
        self.priority = priority

    def __repr__(self):
        return f"Rule({self.name}, priority={self.priority})"


class WorkingMemory:
    def __init__(self, kb: str):
        self.facts = []
        self.rules = []
        self.questions = {}
        self.final_diagnosis = None

        self.load(kb)

    def load(self, path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for f in data.get("facts", []):
            self.facts.append(Fact(f["p"], f["a"], "initial"))

        for r in data.get("rules", []):
            self.rules.append(Rule(r["name"], r["lhs"], r["rhs"], r.get("priority", 0)))

        # вопросы
        self.questions = data.get("questions", {})

    def add_fact(self, fact: Fact):
        if not self.exists(fact.predicate, fact.args):
            self.facts.append(fact)
            return True
        return False

    def remove_fact(self, predicate, args):  # <-- НОВЫЙ МЕТОД
        """Removes a fact matching predicate and args."""
        original_len = len(self.facts)
        # Использование списочного включения для создания нового списка без совпадающих фактов
        self.facts = [
            f for f in self.facts if not (f.predicate == predicate and f.args == args)
        ]
        return len(self.facts) < original_len

    def set_final_diagnosis(self, diagnosis):
        self.final_diagnosis = diagnosis

    def get_final_diagnosis(self):
        return self.final_diagnosis

    def exists(self, predicate, args):
        if args == ["?"]:
            return any(f.predicate == predicate for f in self.facts)
        return any(f.predicate == predicate and f.args == args for f in self.facts)

    def find(self, predicate):
        return [f for f in self.facts if f.predicate == predicate]

    def get_rules(self):
        return self.rules

    def get_questions(self):
        return self.questions

    def __repr__(self):
        return (
            "Facts:\n"
            + "\n".join(str(f) for f in self.facts)
            + "\n\nRules:\n"
            + "\n".join(str(r) for r in self.rules)
        )
