import numpy as np

from data_handler import DataProvider, Scenario


class DecisionCore:

    def __init__(self, scenario: Scenario):
        self._scenario = scenario

    def plurality_model(self):
        votes = [0] * self._scenario.matrix.shape()
        details = []

        for i in range(self.n_experts):
            first_place_idx = np.where(self.matrix[i] == 1)[0][0]
            votes[first_place_idx] += 1
            details.append(
                f"Эксперт {i+1} отдал голос за: {self.candidates[first_place_idx]}"
            )

        max_votes = max(votes)
        winner_idx = votes.index(max_votes)

        for idx, count in enumerate(votes):
            report += f"{self.candidates[idx]}: {count} чел.\n"

        report += f"\nИТОГ: Победил {self.candidates[winner_idx]} с результатом {max_votes} из {self.n_experts}.\n"

        return {"winner": self.candidates[winner_idx], "report": report}


if __name__ == "__main__":
    dp = DataProvider()
    scenario = dp.get_scenario_by_index(1)
    core = DecisionCore(scenario.matrix, scenario.candidates)
    result = core.plurality_model()
    print(result["report"])
