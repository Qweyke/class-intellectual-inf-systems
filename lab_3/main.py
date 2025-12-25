from kb_manager import KBManager
from inference_engine import InferenceEngine


def main():
    kb = KBManager("lab_3/knowledge_base.json")
    engine = InferenceEngine(kb)
    kb.look_up()

    while True:
        print("\n" + "=" * 40)
        print(" TELEMATICS TERMINAL EXPERT SYSTEM")
        print("=" * 40)
        print("1. Check if given node is a '...' ")
        print("2. Find all instances of given node")
        print("3. Determine terminal state by led")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            sub_node = input("\nEnter start-node: ").strip().lower()
            target_node = input("\nEnter node to compare: ").strip().lower()
            engine.is_subject_a_target(sub_node, target_node)

        elif choice == "2":
            node = input("\nEnter node name to find its instances: ").strip().lower()
            engine.get_all_instances_of(node)

        elif choice == "3":
            led_color = input("\nEnter current led_'color': ").strip().lower()
            engine.diagnostic_by_led(led_color)

        elif choice == "4":
            print("Shutting down Expert System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
