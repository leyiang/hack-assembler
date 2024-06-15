import sys
import re
from Parser import Parser
from Code import Code
from utils import log

if len(sys.argv) < 3:
    print("Usage: \n\tpython main.py <asm file path> <compare-test-file>")
    exit()

def assemble(path):
    code = Code()
    parser = Parser( path )
    file = parser.file
    result = []

    while parser.hasMoreLines():
        instrType = parser.instructionType()
        bits = ""

        if instrType is Parser.A_INSTRUCTION:
            symbol = parser.symbol()
            if re.match("^[0-9]", symbol):
                bits = code.ainstr_imm( symbol )
        
        if instrType is Parser.C_INSTRUCTION:
            dest = parser.dest()
            jump = parser.jump()
            comp = parser.comp()
            bits = "111" + code.comp( comp ) + code.dest( dest ) + code.jump( jump )

        parser.advance()
        result.append( bits )
    
    return result

bits = assemble(sys.argv[1])
compareFile = open(sys.argv[2])

for i,raw in enumerate(compareFile):
    compare = raw.strip()
    line = bits[i]
    if line != compare:
        log(f"Test failed at line {i+1} of { sys.argv[2] }")
        print("Your code: \t" + line)
        print("Correct code: \t" + compare)
        break

print("Test Passed for " + sys.argv[2])

raw = "\n".join( bits )
with open("./test.hack", "w") as file:
    file.write( raw )
    
# print( compareFile.readlines() )