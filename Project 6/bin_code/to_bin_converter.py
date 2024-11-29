from bin_code.c_instructions_mapping import DEST, JUMP, COMP


class ToBinConverter:
    @classmethod
    def dest(cls, dest_hack: str) -> str:
        return DEST.get(dest_hack)

    @classmethod
    def jump(cls, jump_hack: str) -> str:
        return JUMP.get(jump_hack)

    @classmethod
    def comp(cls, comp_hack: str) -> str:
        return COMP.get(comp_hack)
