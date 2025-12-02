"""Inference engine: forward-chaining with multiple conflict-resolution strategies."""

from typing import List, Dict, Any
import random
from expert_sys.knowledge_base import Rule


class InferenceEngine:
    def __init__(self, rules: List[Rule], wm, conflict_resolution: str = "specificity"):
        self.rules = rules
        self.wm = wm
        self.conflict_resolution = conflict_resolution
        self.fired_instances = []  # list of dicts with info for explainer
        self.trace = []

    def _match_rule(self, rule: Rule):
        lists = []
        for cond in rule.conditions:
            if cond.strip().lower().startswith("(test"):
                # ignore test for now (could be extended)
                lists.append([{"fact": None, "binding": {}}])
                continue
            m = self.wm.find_matches(cond)
            if not m:
                return []
            lists.append(m)
        all_matches = []

        def combine(idx, cur_bind, cur_facts):
            if idx == len(lists):
                all_matches.append((cur_bind.copy(), list(cur_facts)))
                return
            for match in lists[idx]:
                ok = True
                for k, v in match["binding"].items():
                    if k in cur_bind and cur_bind[k] != v:
                        ok = False
                        break
                if not ok:
                    continue
                nb = cur_bind.copy()
                nb.update(match["binding"])
                nf = list(cur_facts)
                nf.append(match["fact"])
                combine(idx + 1, nb, nf)

        combine(0, {}, [])
        return all_matches

    def _build_agenda(self):
        agenda = []
        for rule in self.rules:
            matches = self._match_rule(rule)
            for bind, facts in matches:
                agenda.append({"rule": rule, "binding": bind, "facts": facts})
        # sort by conflict resolution strategy
        if self.conflict_resolution == "specificity":
            agenda.sort(
                key=lambda e: (
                    -len(e["rule"].conditions),
                    -e["rule"].salience,
                    -max((f["id"] for f in e["facts"]), default=0),
                )
            )
        elif self.conflict_resolution == "recency":
            agenda.sort(key=lambda e: -max((f["id"] for f in e["facts"]), default=0))
        elif self.conflict_resolution == "priority":
            agenda.sort(key=lambda e: -e["rule"].salience)
        elif self.conflict_resolution == "random":
            random.shuffle(agenda)
        return agenda

    def run(self, max_steps: int = 200):
        steps = 0
        while steps < max_steps:
            agenda = self._build_agenda()
            if not agenda:
                break
            entry = agenda.pop(0)
            rule = entry["rule"]
            binding = entry["binding"]
            facts = entry["facts"]
            sig = (rule.name, tuple(sorted(binding.items())))
            if any(fi.get("sig") == sig for fi in self.fired_instances):
                steps += 1
                continue
            # execute actions
            self.trace.append(
                {
                    "step": len(self.fired_instances) + 1,
                    "rule": rule.name,
                    "binding": binding,
                    "facts": [f["id"] for f in facts],
                    "actions": rule.actions,
                }
            )
            for act in rule.actions:
                if act["action"] == "assert":
                    fact = act["fact"]
                    # substitute variables in fact args
                    args = []
                    for a in fact.get("args", []):
                        if isinstance(a, str) and a.startswith("?"):
                            args.append(binding.get(a, a))
                        else:
                            args.append(a)
                    fid = self.wm.assert_fact(fact["predicate"], args, source=rule.name)
                    self.fired_instances.append(
                        {
                            "sig": sig,
                            "derived_fact_id": fid,
                            "rule": rule.name,
                            "binding": binding,
                        }
                    )
                elif act["action"] == "retract":
                    targ = act.get("fact")
                    if targ:
                        args = []
                        for a in targ.get("args", []):
                            if isinstance(a, str) and a.startswith("?"):
                                args.append(binding.get(a, a))
                            else:
                                args.append(a)
                        self.wm.retract_fact(targ["predicate"], args)
                elif act["action"] == "print":
                    print("[PRINT]", act.get("text", ""))
                else:
                    # unknown actions can be extended
                    pass
            steps += 1
        return {"steps": steps, "fired": self.fired_instances, "trace": self.trace}
