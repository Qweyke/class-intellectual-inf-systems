from expert_sys.working_memory import WorkingMemory
from expert_sys.inference_engine import InferenceEngine
from expert_sys.explanation import ExplanationSystem

if __name__ == "__main__":
    print("=== ЭКСПЕРТНАЯ СИСТЕМА: ДИАГНОСТИКА УСТРОЙСТВА ===")

    engine = InferenceEngine(trace=True)

    wm_after, expl_after, final_diag = engine.run()

    print("\n=== ИТОГОВЫЕ ФАКТЫ ===")
    for f in engine.wm.facts:
        print(f)

    if final_diag:
        print("\n=== ДИАГНОЗ ===")
        print(final_diag)

    # Показ объяснения
    engine.expl.show()
