import numpy as np

from data_handler import DataProvider, Scenario


class DecisionCore:
    def __init__(self, scenario: Scenario):
        self._scenario = scenario

    def plurality_model(self):
        option_places = [0] * len(self._scenario.options)
        for expert_id in range(len(self._scenario.experts)):
            for option_id in range(len(self._scenario.matrix[expert_id])):
                if self._scenario.matrix[expert_id][option_id] == 1:
                    option_places[option_id] += 1
                    break

        explanation = "Plurality model analysis:\n"
        max_votes = max(option_places)
        winners_ids = []
        for idx, count in enumerate(option_places):
            if count == max_votes:
                winners_ids.append(idx)
            explanation += f"{self._scenario.options[idx]}: {count} vote(s)\n"

        if len(winners_ids) > 1:
            winners_names = [self._scenario.options[i] for i in winners_ids]
            explanation += f"\nDecision: The winner is not definitely determined. Leaders by the 1-st places taken ({max_votes}): {', '.join(winners_names)}."
        else:
            explanation += f"\nDecision: '{self._scenario.options[winners_ids[0]]}' is a winner. Due to count of 1-st places taken."

        return explanation


if __name__ == "__main__":
    dp = DataProvider()
    scenario = dp._get_scenario_by_index(1)
    core = DecisionCore(scenario)
    result = core.plurality_model()
    print(result)
