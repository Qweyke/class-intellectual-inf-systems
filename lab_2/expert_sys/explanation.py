class ExplanationSystem:
    """Stores rule firing history and diagnostic explanations."""

    def __init__(self, final_diag_fact=None):
        self._events = []
        self.final_diag_fact = final_diag_fact

    def log(self, message: str):
        self._events.append(message)

    def extend(self, messages):
        self._events.extend(messages)

    def get_all(self):
        return list(self._events)

    def clear(self):
        self._events.clear()

    def set_final_diag_fact(self, fact):
        self.final_diag_fact = fact

    def show(self):
        """Displays the explanation."""
        print("\n=== КОМПОНЕНТА ОБЪЯСНЕНИЯ ===")

        if self.final_diag_fact:
            print(
                f"**Для постановки диагноза {self.final_diag_fact.args[0]} использовались следующие шаги и факты:**"
            )
        else:
            print("**Шаги логического вывода:**")

        for i, event in enumerate(self._events):
            print(f"  {i+1}. {event}")

        if not self._events:
            print("  (Нет зафиксированных шагов вывода)")
