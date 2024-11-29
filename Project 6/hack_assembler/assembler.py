from parser.parser import AsmParser
from symbol_table.table import SymbolTable
from bin_code.to_bin_converter import ToBinConverter
from parser.instruction_types import (
    C_INSTRUCTION,
)


class HackAssembler:
    def __init__(self, file_name: str):
        self.symbol_table = SymbolTable()
        self.to_bin = ToBinConverter()
        self.parser = AsmParser(file_name, self.symbol_table)

    def generate_bin_code(self):
        bins = []
        while self.parser.has_more_lines():
            self.parser.advance()
            inst_type = self.parser.get_current_instruction_type()
            if inst_type == C_INSTRUCTION:
                bins.append(self.c_instruction_to_bin())
            else:
                bins.append(self.a_instruction_to_bin())
        return bins

    def c_instruction_to_bin(self):
        comp_hack = self.parser.comp()
        dest_hack = self.parser.dest()
        jump_hack = self.parser.jump()
        return (
            "111"
            + self.to_bin.comp(comp_hack)
            + self.to_bin.dest(dest_hack)
            + self.to_bin.jump(jump_hack)
        )

    def a_instruction_to_bin(self):
        symbol_str = self.parser.symbol()
        is_in_table = self.symbol_table.contains(symbol_str)
        if not is_in_table:
            try:
                symbol_int = int(symbol_str)
                self.symbol_table.add_entry(symbol_str, symbol_int)
            except ValueError:
                self.symbol_table.add_entry(symbol_str)
        address = self.symbol_table.get_address(symbol_str)
        return self.int_to_16_bit(address)

    @staticmethod
    def int_to_16_bit(num: int) -> str:
        return bin(num)[2:].zfill(16)
