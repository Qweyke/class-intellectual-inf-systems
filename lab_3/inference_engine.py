class InferenceEngine:
    def __init__(self, kb_manager):
        self.kb = kb_manager

    def is_subject_a_target(self, subject, target):
        if subject not in self.kb.knowledge:
            print(f"There is no such node as '{subject}'")
            return False

        current_node = subject
        path = []

        while True:
            path.append(current_node)

            if current_node == target:
                print(f"Yes: {' -> '.join(path)}")
                return True

            current_relations = self.kb.get_node_relations(current_node)
            if "is_a" in current_relations:
                current_node = current_relations["is_a"][0]
            else:
                break

        print(f"No: {' -> '.join(path)} - > (X) -> {target}")
        return False

    def get_all_instances_of(self, target):
        results = []

        for node in self.kb.knowledge:
            if node != target and self.is_subject_a_target(node, target):
                results.append(node)

        if results:
            print(f"Types of '{target}': {', '.join(results)}")
        else:
            print(f"No subtypes found for '{target}'")
        return results

    def diagnostic_by_led(self, led_color):
        print(f"\nLed diagnosis: {led_color}")

        error_states = [
            s
            for s, d in self.kb.knowledge.items()
            if "causes" in d and led_color in d["causes"]
        ]

        if not error_states:
            print("No error-state for this color")
            return

        for state in error_states:
            print(f"\nFound state: {state}")
            behaviors = [
                b
                for b, d in self.kb.knowledge.items()
                if "causes" in d and state in d["causes"]
            ]

            for behavior in behaviors:
                user_confirm = input(
                    f"Do you see this behavior: '{behavior}'? (y/n): "
                ).lower()

                if user_confirm == "y":
                    root_causes = [
                        r
                        for r, d in self.kb.knowledge.items()
                        if "causes" in d and behavior in d["causes"]
                    ]

                    for root in root_causes:
                        # Находим метод ремонта
                        fix = self.kb.knowledge.get(root, {}).get(
                            "fix_by", ["no data"]
                        )[0]
                        print(f"\nTrouble in '{root}'")
                        print(f">Fix: {fix.upper()}")
                    return
        print(f"\nNo fix found ")
