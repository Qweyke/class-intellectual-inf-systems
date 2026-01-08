from data_handler import DataProvider, Scenario


class DecisionCore:
    def __init__(self, scenario: Scenario):
        self._scenario = scenario

        self._condorcet_matrix = self._assemble_duel_matrix()

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

    def _assemble_duel_matrix(self):
        n = len(self._scenario.options)
        result_matrix = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if j == i:
                    result_matrix[i][j] = "-"
                    continue

                votes_for_i = 0
                for expert_row in self._scenario.matrix:
                    if expert_row[i] < expert_row[j]:
                        votes_for_i += 1

                result_matrix[i][j] = votes_for_i

        return result_matrix

    def condorcet_clear_winner_rule(self):
        n = len(self._scenario.options)
        explanation = "Condorcet clear winner analysis:\n"

        for i in range(n):
            for j in range(i + 1, n):
                opt_i = self._scenario.options[i]
                opt_j = self._scenario.options[j]
                explanation += f"{opt_i} vs {opt_j}: {self._condorcet_matrix[i][j]} - {self._condorcet_matrix[j][i]}\n"

        winner_idx = None

        for i in range(n):
            is_winner = True
            for j in range(n):
                if i == j:
                    continue

                if self._condorcet_matrix[i][j] <= self._condorcet_matrix[j][i]:
                    is_winner = False
                    break

            if is_winner:
                winner_idx = i
                break

        explanation += "\nDecision: "
        if winner_idx is not None:
            winner_name = self._scenario.options[winner_idx]
            explanation += f"'{winner_name}' is the clear winner. This candidate won all pairwise duels against other options."
        else:
            explanation += "No clear winner found. A 'Condorcet Paradox' (voting cycle) or a tie exists. Use Copeland or Simpson rules."

        return explanation

    def condorcet_copeland_rule(self):
        n = len(self._scenario.options)
        copeland_indices = [0] * n
        explanation = "Copeland's rule analysis (Wins - Losses):\n"

        for i in range(n):
            wins = 0
            losses = 0
            draws = 0
            opt_i = self._scenario.options[i]

            for j in range(n):
                if i == j:
                    continue

                if self._condorcet_matrix[i][j] > self._condorcet_matrix[j][i]:
                    wins += 1
                elif self._condorcet_matrix[i][j] < self._condorcet_matrix[j][i]:
                    losses += 1
                else:
                    draws += 1

            copeland_indices[i] = wins - losses
            explanation += f"{opt_i}: {wins} wins, {losses} losses, {draws} draws. Index: {copeland_indices[i]}\n"

        max_score = max(copeland_indices)
        winners_ids = [
            idx for idx, val in enumerate(copeland_indices) if val == max_score
        ]

        explanation += "\nDecision: "
        if len(winners_ids) > 1:
            names = [self._scenario.options[idx] for idx in winners_ids]
            explanation += f"Tie between {', '.join(names)} with score {max_score}."
        else:
            winner_name = self._scenario.options[winners_ids[0]]
            explanation += f"'{winner_name}' is the winner by Copeland's rule with score {max_score}."

        return explanation

    def condorcet_simpson_rule(self):
        n = len(self._scenario.options)
        min_supports = []
        explanation = "Simpson's minimax rule analysis (Maximizing minimum support):\n"

        for i in range(n):
            opt_i = self._scenario.options[i]
            supports_for_i = []

            for j in range(n):
                if i == j:
                    continue
                supports_for_i.append(self._condorcet_matrix[i][j])

            worst_performance = min(supports_for_i)
            min_supports.append(worst_performance)

            explanation += (
                f"{opt_i}: minimal support in duels is {worst_performance} vote(s).\n"
            )

        max_min_support = max(min_supports)
        winners_ids = [
            idx for idx, val in enumerate(min_supports) if val == max_min_support
        ]

        explanation += "\nDecision: "
        if len(winners_ids) > 1:
            winners_names = [self._scenario.options[idx] for idx in winners_ids]
            explanation += (
                f"Tie between {', '.join(winners_names)}. "
                f"All of them have the same minimal support level ({max_min_support})."
            )
        else:
            winner_name = self._scenario.options[winners_ids[0]]
            explanation += (
                f"'{winner_name}' is the winner by Simpson's rule. "
                f"Even in their most difficult comparison, '{winner_name}' kept the highest level "
                f"of support among all candidates ({max_min_support} vote(s))."
            )

        explanation += f"\n\n{self._condorcet_matrix}"
        return explanation

    def borda_model(self):
        n = len(self._scenario.options)
        borda_scores = [0] * n
        explanation = "Borda count analysis (Positional scoring):\n"

        explanation += f"Scoring system: 1st place = {n-1} pts, last place = 0 pts.\n\n"

        for i in range(n):
            total_points = 0
            opt_name = self._scenario.options[i]

            for expert_row in self._scenario.matrix:
                rank = expert_row[i]
                points = n - rank
                total_points += points

            borda_scores[i] = total_points
            explanation += f"{opt_name}: {total_points} total points\n"

        max_score = max(borda_scores)
        winners_ids = [idx for idx, val in enumerate(borda_scores) if val == max_score]

        explanation += "\nDecision: "
        if len(winners_ids) > 1:
            names = [self._scenario.options[idx] for idx in winners_ids]
            explanation += f"Tie between {', '.join(names)} with {max_score} points."
        else:
            winner_name = self._scenario.options[winners_ids[0]]
            explanation += f"'{winner_name}' is the winner by Borda count. This option has the highest overall consensus among experts."

        return explanation


if __name__ == "__main__":
    dp = DataProvider()
    scenario = dp._get_scenario_by_index(1)
    core = DecisionCore(scenario)
    # result = core.plurality_model()
    result = core.borda_model()
    print(result)
