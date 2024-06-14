class Parser:
    A_INSTRUCTION=0
    C_INSTRUCTION=1
    L_INSTRUCTION=2

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
        return "";

    def dest(self) -> str:
        return "";

    def comp(self) -> str:
        return "";

    def jump(self) -> str:
        return "";