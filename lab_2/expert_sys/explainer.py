"""Explainer: decoupled from WM; uses trace + WM to answer WHY/HOW."""

from typing import List, Dict, Any


class Explainer:
    def __init__(self, wm, trace: List[Dict[str, Any]]):
        self.wm = wm
        self.trace = trace

    def how(self) -> str:
        s = "Execution trace:\n"
        for st in self.trace:
            s += f" Step {st['step']}: rule {st['rule']} fired\n   Bindings: {st['binding']}\n   Matched facts: {st['facts']}\n   Actions: {st['actions']}\n"
        return s

    def why(self, predicate: str, args: List[str] = None) -> str:
        # find fact in WM
        matches = [
            f
            for f in self.wm.facts
            if f["predicate"] == predicate and (args is None or f["args"] == args)
        ]
        if not matches:
            return "Fact not in working memory."
        fact = matches[0]
        # find which trace steps asserted this fact
        derivs = []
        for st in self.trace:
            for a in st.get("actions", []):
                if a.get("action") == "assert":
                    fa = a.get("fact")
                    if fa and fa["predicate"] == predicate:
                        derivs.append(st)
        if not derivs:
            return "Fact present but no derivation recorded (may be initial fact)."
        s = f"Derivation for fact {predicate} {fact['args']}:\n"
        for st in derivs:
            s += f" Rule {st['rule']} at step {st['step']} with bindings {st['binding']}\n"
        return s
