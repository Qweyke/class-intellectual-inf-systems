"""I/O: load KB (JSON), handle questions (interactive or scripted)."""

import json
from typing import Dict, Any, List, Optional


def load_kb(path: str) -> Dict[str, Any]:
    """Load KB from a JSON file and return a dictionary structure."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_questions(kb: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Return the list of questions defined in KB (may be empty)."""
    return kb.get("questions", [])


def ask_questions(questions: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Interactively ask questions listed in the KB. Return list of asserted facts as dicts."""
    answers = []
    for q in questions:
        prompt = q.get("prompt", f"Question about {q.get('id','?')}")
        choices = q.get("choices")
        if choices:
            prompt += " (" + "/".join(choices) + ")"
        prompt += ": "
        default = q.get("default")
        if default is not None:
            ans = default
            print(f"{prompt}{ans}  [default used]")
        else:
            ans = input(prompt).strip()
        fact = {"predicate": q["predicate"], "args": [ans], "source": "user"}
        answers.append(fact)
    return answers
