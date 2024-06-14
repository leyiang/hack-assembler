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
    
    def _instrOnlyFor(self, types, methodName):
        if len(types) == 0:
            raise Exception("You need to put at least one type in types array")

        instrType = self.instructionType()

        if instrType not in types:
            typeLables = map(lambda x: Parser.INSTRUCTION_TYPE_LABEL[x], types)
            typeLables = "&".join( typeLables )
            raise Exception(f"Only { typeLables } Instruction can call { methodName }()")

        return instrType

    def symbol(self) -> str:
        instrType = self._instrOnlyFor([
            self.A_INSTRUCTION,
            self.L_INSTRUCTION
        ], "symbol");

        if instrType == self.A_INSTRUCTION:
            return self.line[1:]
        elif instrType == self.L_INSTRUCTION:
            return self.line[1:-1]

    def dest(self) -> str:
        self._instrOnlyFor([self.C_INSTRUCTION], "dest")

        eqSignPos = self.line.find("=")

        if eqSignPos <= -1:
            return "null"
        else:
            return self.line[:eqSignPos]

    def comp(self) -> str:
        self._instrOnlyFor([self.C_INSTRUCTION], "jump")
        eqPos = self.line.find("=")
        eqPos = 0 if eqPos < 0 else eqPos + 1

        scPos = self.line.find(";")
        scPos = len(self.line) if scPos < 0 else scPos

        compRaw = self.line[eqPos:scPos]

        return compRaw

    def jump(self) -> str:
        self._instrOnlyFor([self.C_INSTRUCTION], "jump")

        scPos = self.line.find(";")
        if scPos <= -1:
            return "null"
        elif scPos == len(self.line) -1:
            raise Exception("Syntax Error: no jump found after semicolon, line: " + self.line)
        else:
            return self.line[scPos+1:]