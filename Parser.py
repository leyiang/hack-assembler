class Parser:
    A_INSTRUCTION=0
    C_INSTRUCTION=1
    L_INSTRUCTION=2

    INSTRUCTION_TYPE_LABEL=["A", "C", "L"]

    def __init__(self, file_path) -> None:
        self.file = open(file_path, "r")
        self.line = ""
        self.skip()

    def hasMoreLines(self) -> bool:
        return bool( self.line )

    # Skip Comments and White spaces
    def skip(self):
        while True:
            try:
                line = next(self.file)
                line = line.strip()
                toSkip = line.startswith("//") or (not line)

                if not toSkip:
                    self.line = line
                    break
            except StopIteration:
                self.line = None
                break
        
    def advance(self):
        self.skip()

    def instructionType(self) -> int:
        if self.line[0] == "@":
            return self.A_INSTRUCTION
        elif self.line[0] == "(":
            return self.L_INSTRUCTION
        else:
            return self.C_INSTRUCTION
    
    def symbol(self) -> str:
        instrType = self.instructionType()

        if instrType == self.A_INSTRUCTION:
            return self.line[1:]
        elif instrType == self.L_INSTRUCTION:
            return self.line[1:-1]
        else:
            raise Exception("Only A & L Instruction can call symbol()")

    def dest(self) -> str:
        instrType = self.instructionType()

        if instrType == self.C_INSTRUCTION:
            eqSignPos = self.line.find("=")

            if eqSignPos <= -1:
                return "null"
            else:
                return self.line[:eqSignPos]
        else:
            raise Exception("Only C Instruction can call dest()")

    def comp(self) -> str:
        return "";

    def jump(self) -> str:
        return "";