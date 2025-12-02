from expert_sys.communicator import load_kb, get_questions, ask_questions
from expert_sys.knowledge_base import load_rules_from_kb
from expert_sys.working_memory import WorkingMemory
from expert_sys.inference_engine import InferenceEngine
from expert_sys.explainer import Explainer


def main():
    kb = load_kb("lab_2/telematics_diag.json")

    print("\n=== Expert System Started ===")

    # Working memory
    wm = WorkingMemory()

    # Load initial facts
    for f in kb.get("facts", []):
        wm.assert_fact(f["predicate"], f["args"], source=f.get("source"))

    # Ask questions interactively
    questions = get_questions(kb)
    for q in questions:
        print(f"\nQuestion: {q['question']}")
        if q.get("options"):
            print("Options:", ", ".join(q["options"]))

        user_input = input("Your answer: ").strip()

        # if fact has no args – treat answer as string
        wm.assert_fact(q["ask"], [user_input], source="user")

    # Load production rules
    rules = load_rules_from_kb(kb)

    # Inference engine
    engine = InferenceEngine(rules, wm, conflict_resolution="specificity")
    result = engine.run(max_steps=100)

    print("\n=== Inference Finished ===")
    print("Final working memory:")
    print(wm.pretty())

    # Final answers to user
    print("\n=== Conclusions ===")
    conclusions = [f for f in wm.facts if f["source"] not in ("user", "initial")]
    for c in conclusions:
        print(f" * {c['predicate']}({', '.join(c['args'])})")

    # Explanation module
    expl = Explainer(wm, result["trace"])

    print("\n=== How the result was reached ===")
    print(expl.how())


if __name__ == "__main__":
    main()
