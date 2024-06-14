# coffee size: S (Rp7k), M (Rp10k), L (Rp12k)
# coffee menu: americano, caffe latte, cappuccino, macchiato, palm sugar
# coffee variants: hot, cold
# steps: (q0) pick size, (q1) payment, (q2) pick menu, (q3) hot or cold, (q4) deliver


class FSA:
    def __init__(self):
        self.states = {"Q0", "Q1", "Q2", "Q3", "Q4"}
        self.sigma = {"a", "b", "c", "d", "e"}
        self.initial_state = "Q0"
        self.final_state = {"Q4"}
        self.current_state = self.initial_state
        self.delta = {
            ("Q0", "a"): "Q1",
            ("Q0", "b"): "Q1",
            ("Q0", "c"): "Q1",
            ("Q1", "a"): "Q2",
            ("Q1", "b"): "Q0",
            ("Q2", "a"): "Q3",
            ("Q2", "b"): "Q3",
            ("Q2", "c"): "Q3",
            ("Q2", "d"): "Q3",
            ("Q2", "e"): "Q3",
            ("Q3", "a"): "Q4",
            ("Q3", "b"): "Q4",
            ("Q3", "c"): "Q2",
        }
        self.inputted_symbols = []

    def transition(self, input_symbol):
        if (self.current_state, input_symbol) in self.delta:
            self.current_state = self.delta[(self.current_state, input_symbol)]
            self.inputted_symbols.append(input_symbol)
            print(f"\nTransitioned to {self.current_state}")
        else:
            print(
                f"\nInvalid choice from {self.current_state} with input {input_symbol}"
            )

    def is_accepted(self):
        return self.current_state in self.final_state

    def get_inputted_string(self):
        return "".join(self.inputted_symbols)


fsa = FSA()
while not fsa.is_accepted():
    print(f"\nCurrent state: {fsa.current_state}")

    if fsa.current_state == "Q0":
        print("Pick A Size:\na. S (Rp7k)\nb. M (Rp10k)\nc. L (Rp12k)\nd. Cancel (exit)")
        input_symbol = input("Your Choice: ").lower()
        if input_symbol == "d":
            print("Purchase cancelled.\n")
            break
    elif fsa.current_state == "Q1":
        print("Proceed:\na. Insert Money\nb. Back\nc. Cancel (exit)")
        input_symbol = input("Your Choice: ").lower()
        if input_symbol == "c":
            print("Purchase cancelled.\n")
            break
    elif fsa.current_state == "Q2":
        print(
            "Menu:\na. Americano\nb. Caffe Latte\nc. Cappuccino\nd. Macchiato\ne. Palm Sugar Coffee"
        )
        input_symbol = input("Your Choice: ").lower()
    elif fsa.current_state == "Q3":
        print("Variant:\na. Hot\nb. Cold\nc. Back")
        input_symbol = input("Your Choice: ").lower()

    if input_symbol not in fsa.sigma:
        print("Invalid choice. Please try again.")
        continue

    fsa.transition(input_symbol)

if fsa.is_accepted():
    print("\nThe purchase process is complete. Enjoy your Coffee.")
    print(f"Purchase ID: {fsa.get_inputted_string()}\n")
