import sys
import re
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
    bits = ""

    if instrType is not Parser.C_INSTRUCTION:
        print("\tSymbol: [" + parser.symbol() + "]")
    
    if instrType is Parser.A_INSTRUCTION:
        symbol = parser.symbol()
        if re.match("^[0-9]", symbol):
            bits = code.ainstr_imm( symbol )
            print("\tBits: ", bits)
    
    if instrType is Parser.C_INSTRUCTION:
        dest = parser.dest()
        jump = parser.jump()
        comp = parser.comp()

        print("\tDest: ", dest, code.dest( dest ) )
        print("\tJump: ", jump, code.jump( jump ) )
        print("\tComp: ", comp, code.comp( comp ) )
        bits = "111" + code.dest( dest ) + code.jump( jump ) + code.comp( comp ) 

        print("\tBits: ", bits )
    parser.advance()