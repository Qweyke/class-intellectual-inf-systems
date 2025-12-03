from expert_sys.working_memory import Fact, WorkingMemory
from expert_sys.explanation import ExplanationSystem


class InferenceEngine:

    def __init__(self, trace=True):
        self.wm = WorkingMemory("lab_2/test.json")
        self.expl = ExplanationSystem()
        self.trace = trace

    def log(self, msg):
        if self.trace:
            print(msg)

    def ask_user(self, qid):
        q = self.wm.get_questions()[qid]
        question = q["question"]
        answers = q["answers"]

        print(f"\n{question}")
        for i, a in enumerate(answers):
            print(f"{i+1}) {a}")

        while True:
            x = input("Ваш ответ: ")
            if x.isdigit() and 1 <= int(x) <= len(answers):
                selected_answer = answers[int(x) - 1]

                self.expl.log(
                    f'Запрос факта: "{question}" -> Ответ пользователя: "{selected_answer}"'
                )

                return selected_answer
            print("Некорректный ввод!")

    def match_lhs(self, rule):
        matched = []
        for p in rule.lhs:
            pred = p["p"]
            args = p["a"]

            if "ask" in p:
                if args == ["unknown"] and self.wm.exists(pred, args):

                    ans = self.ask_user(p["ask"])

                    self.wm.remove_fact(pred, args)
                    self.log(
                        f"(REMOVE) {pred}{tuple(args)} - Заменен ответом пользователя"
                    )

                    nf = Fact(pred, [ans], "user")
                    self.wm.add_fact(nf)
                    self.log(f"(ADD) {nf}")

                    matched.append(p)
                    continue

            found_current = self.wm.find(pred)

            ok = any(f.args == args or args == ["?"] for f in found_current)

            if not ok:
                return None

            matched.append(p)

        return matched

    def build_agenda(self):
        agenda = []
        for r in self.wm.get_rules():
            res = self.match_lhs(r)
            if res and not self.wm.exists(r.rhs["p"], r.rhs["a"]):
                agenda.append((r, res))
        return agenda

    def conflict_resolution(self, agenda):
        agenda.sort(key=lambda x: x[0].priority, reverse=True)
        return agenda[0]

    def fire(self, rule, matched):
        rhs = rule.rhs
        f = Fact(rhs["p"], rhs["a"], rule.name)

        if self.wm.add_fact(f):
            conditions = ", ".join(f'{p["p"]}{tuple(p["a"])}' for p in matched)
            self.expl.log(
                f"Сработало правило [{rule.name}]: ЕСЛИ {conditions} ТО {f}. (Приоритет: {rule.priority})"
            )

            self.log(f"[{rule.name}] -> {f}")

            if rhs["p"] == "diagnosis":
                self.wm.set_final_diagnosis(f)
                self.expl.set_final_diag_fact(f)
                return True
        return False

    def run(self):
        self.log("\n=== ЗАПУСК ДВИЖКА ===")

        while True:
            agenda = self.build_agenda()
            if not agenda:
                self.log("=== ВЫВОД ЗАВЕРШЕН ===")
                break

            rule, matched = self.conflict_resolution(agenda)

            if self.fire(rule, matched):
                self.log("=== ДИАГНОЗ ПОЛУЧЕН ===")
                break

        return self.wm, self.expl, self.wm.get_final_diagnosis()
