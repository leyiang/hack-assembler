import sys
from Parser import Parser

if len(sys.argv) < 2:
    print("Usage: \n\tpython main.py <asm file path>")
    exit()

parser = Parser( sys.argv[1] )
file = parser.file

while parser.hasMoreLines():
    print( parser.line, parser.instructionType() )

    if parser.instructionType() is not Parser.C_INSTRUCTION:
        print("Symbol: [" + parser.symbol() + "]")

    parser.advance()