import sys
from Parser import Parser

if len(sys.argv) < 2:
    print("Usage: \n\tpython main.py <asm file path>")
    exit()

parser = Parser( sys.argv[1] )
file = parser.file

while parser.hasMoreLines():
    instrType = parser.instructionType()
    print( f"({Parser.INSTRUCTION_TYPE_LABEL[instrType]})", parser.line )

    if instrType is not Parser.C_INSTRUCTION:
        print("\tSymbol: [" + parser.symbol() + "]")
    
    if instrType is Parser.C_INSTRUCTION:
        print("\tDest: ", parser.dest() )

    if instrType is Parser.C_INSTRUCTION:
        print("\tJump: ", parser.jump() )

    parser.advance()