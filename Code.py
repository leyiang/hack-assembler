class Code:
    JUMP_MAP = {
        "null": "000",
        "JGT" : "001",
        "JEQ" : "010",
        "JGE" : "011",
        "JLT" : "100",
        "JNE" : "101",
        "JLE" : "110",
        "JMP" : "111",
    }

    def __init__(self):
        pass
    
    def dest(self, raw) -> str:
        bits = [0] * 3
        used = [0] * 3

        allowed = {
            "A": 0,
            "D": 1,
            "M": 2,
        }

        if raw != "null":
            for ch in raw:
                if ch not in allowed:
                    raise Exception("Invalid Destination")
                index = allowed[ch]
                if used[index]:
                    raise Exception("Invalid Destination")

                bits[index] = 1
                used[index] = 1

        return "".join(map(str, bits))

    def comp(self) -> str:
        pass

    def jump(self, raw) -> str:
        if raw not in Code.JUMP_MAP:
            raise Exception("Invalid Jump Expression")
        return Code.JUMP_MAP[ raw ]