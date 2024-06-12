"""
This program is used only to check the validity of the
Purchase ID from the Coffee Machine program
"""


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

    def diterima(self, string_input):
        state_sekarang = self.initial_state

        for simbol in string_input:
            if (state_sekarang, simbol) in self.delta:
                print(f"State saat ini: {state_sekarang}. Input: {simbol}")
                state_sekarang = self.delta[(state_sekarang, simbol)]
            else:
                return False

        return state_sekarang in self.final_state

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
string_input = input("String yang ingin dibaca: ")
print("")
if fsa.diterima(string_input):
    print(f'\nHASIL AKHIR: String "{string_input}" diterima.')
else:
    print(f'\nHASIL AKHIR: String "{string_input}" ditolak.')


# if fsa.diterima():
#     print("\nThe purchase process is complete. Enjoy your Coffee.")
#     print(f"Purchase ID: {fsa.get_inputted_string()}")


# class Dfa:
#     def __init__(self):
#         self.state = {"Q0", "Q1", "Q2", "Q3"}
#         self.simbol_input = {"a", "b"}
#         self.state_awal = "Q0"
#         self.state_akhir = {"Q3"}
#         self.fungsi_transisi = {
#             ("Q0", "a"): "Q1",
#             ("Q0", "b"): "Q0",
#             ("Q1", "a"): "Q2",
#             ("Q1", "b"): "Q0",
#             ("Q2", "a"): "Q3",
#             ("Q2", "b"): "Q1",
#             ("Q3", "a"): "Q3",
#             ("Q3", "b"): "Q2",
#         }

#     def diterima(self, string_input):
#         state_sekarang = self.state_awal

#         for simbol in string_input:
#             if (state_sekarang, simbol) in self.fungsi_transisi:
#                 print(f"State saat ini: {state_sekarang}. Input: {simbol}")
#                 state_sekarang = self.fungsi_transisi[(state_sekarang, simbol)]
#             else:
#                 return False

#         return state_sekarang in self.state_akhir


# dfa = Dfa()
# string_input = input("String yang ingin dibaca: ")
# print("")
# if dfa.diterima(string_input):
#     print(f'\nHASIL AKHIR: String "{string_input}" diterima.')
# else:
#     print(f'\nHASIL AKHIR: String "{string_input}" ditolak.')
