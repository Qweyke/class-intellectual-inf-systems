"""Knowledge base structures: Rule and a simple loader for JSON KB."""

from typing import List, Dict, Any


class Rule:
    """
    Rule representation.
    Fields:
      - name: unique rule id
      - conditions: list of condition strings, e.g. "(power ?x)"
      - actions: list of actions: {"action":"assert","fact":{"predicate":...,"args":[...]}} or retract/print
      - salience: integer priority
    """

    def __init__(
        self,
        name: str,
        conditions: List[str],
        actions: List[Dict[str, Any]],
        salience: int = 0,
        metadata: Dict[str, Any] = None,
    ):
        self.name = name
        self.conditions = conditions
        self.actions = actions
        self.salience = salience
        self.metadata = metadata or {}

    def __repr__(self):
        return f"<Rule {self.name} sal={self.salience} conds={len(self.conditions)}>"


def load_rules_from_kb(kb: Dict[str, Any]) -> List[Rule]:
    rules = []
    for r in kb.get("rules", []):
        rules.append(
            Rule(
                r["name"],
                r.get("conditions", []),
                r.get("actions", []),
                r.get("salience", 0),
                r.get("metadata", {}),
            )
        )
    return rules
