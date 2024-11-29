import os

from symbol_table.table import SymbolTable
from parser.instruction_types import (
    A_INSTRUCTION,
    C_INSTRUCTION,
    L_INSTRUCTION,
)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASM_DIR = os.path.join(BASE_DIR, "tests", "asmFiles")


class AsmParser:
    def __init__(self, file_name: str, symbol_table: SymbolTable):
        self._table = symbol_table
        self._instructions = []
        self._current_instruction_index = -1
        self._current_instruction = ""
        file = ASM_DIR + "/" + file_name
        try:
            with open(file, "r") as f:
                self._raw_file = f.read()
                self.extract_instructions()
        except FileNotFoundError as e:
            raise e

    def extract_instructions(self):
        for line in self._raw_file.splitlines():
            comments_idx = line.find("//")
            any_comments = comments_idx >= 0

            instruction = (
                line[:comments_idx].strip() if any_comments else line.strip()
            )

            if not instruction:
                continue
            self.process_instruction(instruction, self._table)

    def process_instruction(self, instruction: str, table: SymbolTable):
        inst_type = self.get_instruction_type(instruction)

        symbol = self.get_symbol(instruction)
        if not table.contains(symbol) and inst_type == L_INSTRUCTION:
            table.add_entry(symbol, len(self._instructions))
            return None
        self._instructions.append(instruction)

    def has_more_lines(self):
        has_more_lines = self._current_instruction_index < len(self._instructions) - 1
        if has_more_lines and self._instructions:
            return True
        return False

    def advance(self) -> str:
        if self.has_more_lines():
            self._current_instruction_index += 1
            self._current_instruction = self._instructions[
                self._current_instruction_index
            ]
        return self._current_instruction

    def get_current_instruction_type(self) -> str:
        return self.get_instruction_type(
            self._current_instruction
        )

    def symbol(self) -> str:
        self.check_is_c_instruction()
        return self.get_symbol(self._current_instruction)

    def get_symbol(self, instruction: str) -> str:
        inst_type = self.get_instruction_type(instruction)
        if inst_type == A_INSTRUCTION:
            return instruction[1:]
        return instruction[1:-1]

    def dest(self) -> str | None:
        self.check_is_not_c_instruction()

        eq_sign_idx = self._current_instruction.find("=")
        if eq_sign_idx != -1:
            return self._current_instruction[:eq_sign_idx]
        return None

    def jump(self) -> str | None:
        self.check_is_not_c_instruction()

        semicolon_idx = self._current_instruction.find(";")
        if semicolon_idx != -1:
            return self._current_instruction[-3:]
        return None

    def comp(self) -> str:
        self.check_is_not_c_instruction()

        eq_sign_idx = self._current_instruction.find("=")
        if eq_sign_idx != -1:
            return self._current_instruction[eq_sign_idx + 1 :]
        else:
            semicolon_idx = self._current_instruction.find(";")
            return self._current_instruction[:semicolon_idx]

    def check_is_c_instruction(self):
        if self.get_current_instruction_type() == C_INSTRUCTION:
            raise Exception(
                f"Only can be called with {A_INSTRUCTION!r} or {L_INSTRUCTION!r}!"
            )

    @staticmethod
    def get_instruction_type(instruction: str) -> str:
        if instruction.startswith("@"):
            return A_INSTRUCTION
        elif instruction.startswith("(") and instruction.endswith(")"):
            return L_INSTRUCTION
        else:
            return C_INSTRUCTION

    def check_is_not_c_instruction(self):
        if self.get_current_instruction_type() != C_INSTRUCTION:
            raise Exception(f"Only can be called with {C_INSTRUCTION!r}!")
