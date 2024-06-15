from utils import log

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

    COMP_TABLE = {
        "0":   "101010",
        "1":   "111111",
        "-1":  "111010",
        "D":   "001100",

        "A":   "110000",
        "M":   "110000",
        "!D":  "001101",
        "!A":  "110001",
        "!M":  "110001",
        "-D":  "001111",
        "-A":  "110011",
        "-M":  "110011",
        "D+1": "011111",
        "A+1": "110111",
        "M+1": "110111",
        "D-1": "001110",
        "A-1": "110010",
        "M-1": "110010",
        "D+A": "000010",
        "D+M": "000010",
        "D-A": "010011",
        "D-M": "010011",
        "A-D": "000111",
        "M-D": "000111",
        "D&A": "000000",
        "D&M": "000000",
        "D|A": "010101",
        "D|M": "010101",
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

    def comp(self, raw) -> str:
        a = '0' # a bit in "acccccc"

        if "M" in raw:
            a = '1'
        
        if raw not in Code.COMP_TABLE:
            raise Exception("Invalid comp expression")
        
        return a + Code.COMP_TABLE[ raw ]
        
        
    # try to analyze the comp but failed
    # def comp(self, raw) -> str:
    #     operators = "+-!&|"
    #     operands = "01ADM"
    #     allowed = operators + operands
    #     bits = [0] * 7

    #     op, a, b = None, None, None

    #     for ch in raw:
    #         if ch not in allowed:
    #             raise Exception("Invalid comp expression")
            
    #         if ch in operators:
    #             if op is not None:
    #                 raise Exception("Invalid comp expression")
    #             op = ch
    #         else:
    #             if a is None:
    #                 a = ch
    #             elif b is None:
    #                 b = ch
    #             else:
    #                 raise Exception("Invalid comp expression")
            
    #         # the a bit in "acccccc"
    #         if ch == "M":
    #             bits[0] = 1

    #     # D+M
    #     if (op is not None) and (a is not None) and (b is not None):
    #         pass
    #     # +1, -M etc
    #     elif (op is not None) and (a is not None):
    #         pass
    #     # can't happen
    #     elif (op is not None) and (b is not None):
    #         raise Exception("Invalid comp expression")
    #     elif (a is not None) and (b is not None):
    #         raise Exception("Invalid comp expression")
    #     # only one operand should only inside a
    #     elif (b is not None):
    #         raise Exception("Invalid comp expression")
    #     # D
    #     else:
    #         pass
    #     log( op, a, b )

    def jump(self, raw) -> str:
        if raw not in Code.JUMP_MAP:
            raise Exception("Invalid Jump Expression")
        return Code.JUMP_MAP[ raw ]
    
    def ainstr_imm(self, raw) -> str:
        return format(int(raw), '016b')
