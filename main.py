import sys
from Parser import Parser
from Code import Code

if len(sys.argv) < 2:
    print("Usage: \n\tpython main.py <asm file path>")
    exit()

code = Code()
parser = Parser( sys.argv[1] )
file = parser.file

while parser.hasMoreLines():
    instrType = parser.instructionType()
    print( f"({Parser.INSTRUCTION_TYPE_LABEL[instrType]})", parser.line )

    if instrType is not Parser.C_INSTRUCTION:
        print("\tSymbol: [" + parser.symbol() + "]")
    
    if instrType is Parser.C_INSTRUCTION:
        dest = parser.dest()
        print("\tDest: ", dest, code.dest( dest ) )
        print("\tJump: ", parser.jump() )
        print("\tComp: ", parser.comp() )

    parser.advance()