"""Working memory module — stores facts, supports assert/retract and pattern matching."""

from typing import List, Dict, Any, Optional


class WorkingMemory:
    def __init__(self):
        # facts: list of dicts {"id":int,"predicate":str,"args":list,"source":str}
        self.facts: List[Dict[str, Any]] = []
        self._next_id = 1

    def assert_fact(
        self, predicate: str, args: List[str], source: Optional[str] = None
    ) -> int:
        # avoid duplicate by content
        for f in self.facts:
            if f["predicate"] == predicate and f["args"] == args:
                return f["id"]
        fid = self._next_id
        self._next_id += 1
        fact = {"id": fid, "predicate": predicate, "args": args, "source": source}
        self.facts.append(fact)
        return fid

    def retract_fact(self, predicate: str, args: List[str]) -> int:
        before = len(self.facts)
        self.facts = [
            f
            for f in self.facts
            if not (f["predicate"] == predicate and f["args"] == args)
        ]
        return before - len(self.facts)

    def find_matches(self, pattern: str):
        """
        Pattern syntax: "(pred x y)". Variables start with '?'. Returns list of dicts {"fact":fact,"binding":{var:val}}
        """
        pat = pattern.strip()
        if pat.startswith("(") and pat.endswith(")"):
            pat = pat[1:-1].strip()
        parts = pat.split()
        pred = parts[0]
        vars_or_vals = parts[1:]
        matches = []
        for f in self.facts:
            if f["predicate"] != pred:
                continue
            if len(vars_or_vals) != len(f["args"]):
                continue
            binding = {}
            ok = True
            for pv, av in zip(vars_or_vals, f["args"]):
                if pv.startswith("?"):
                    binding[pv] = av
                else:
                    if pv != av:
                        ok = False
                        break
            if ok:
                matches.append({"fact": f, "binding": binding})
        return matches

    def pretty(self):
        return [
            (f["id"], f["predicate"], f["args"], f.get("source")) for f in self.facts
        ]
