# SymbolTable:
# symbol | address
# R0     | 0
# . . . . . . . .


class SymbolTable:
    def __init__(self):
        self.next_free_memory = 16
        self.table = {
            "R0": 0, "SP": 0,
            "R1": 1, "LCL": 1,
            "R2": 2, "ARG": 2,
            "R3": 3, "THIS": 3,
            "R4": 4, "THAT": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SCREEN": 16384,
            "KBD": 24576,
        }

    def add_entry(self, symbol: str, address: int | None = None) -> None:
        if address is None:
            address = self.next_free_memory
            self.next_free_memory += 1
        self.table[symbol] = address

    def contains(self, symbol: str) -> bool:
        return symbol in self.table

    def get_address(self, symbol: str) -> int:
        return self.table[symbol]
