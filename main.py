import sys
import re
from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable
from utils import log

if len(sys.argv) < 3:
    print("Usage: \n\tpython main.py <asm file path> <compare-test-file>")
    exit()

# build symbol table for:
#   built-in symbols like: SCREEN, KBD, etc
#   jump labels: (LOOP)

PREDEFINED_SYMBOLS = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576
} 

def forEveryLine( path, fn ): 
    assert callable(fn), "callback for <forEveryLine> has to be callable"
    parser = Parser(path)
    while parser.hasMoreLines():
        fn( parser )
        parser.advance()


def buildSymbolTable( path ) -> SymbolTable:
    symTable = SymbolTable()

    # R0-R15 = 0-15
    for i in range(16):
        symbol = f"R{i}"
        assert not symTable.contains(symbol), "pre-defined symbols is defined while init, something wrong."
        symTable.addEntry( symbol, i )

    for symbol, addr in PREDEFINED_SYMBOLS.items():
        assert not symTable.contains(symbol), "pre-defined symbols is defined while init, something wrong."
        symTable.addEntry( symbol, addr )

    def addLabelSymbol( parser: Parser ):
        if parser.instructionType() == Parser.L_INSTRUCTION:
            assert not symTable.contains( parser.symbol() ), "label should not define twice"
            symTable.addEntry( parser.symbol(), parser.lineNo + 1 )

    forEveryLine( path, addLabelSymbol )
    return symTable

def assemble(path):
    symTable = buildSymbolTable( path )

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
            else:
                # bits = code.ainstr_imm( )
                if symTable.contains( symbol ):
                    bits = code.ainstr_imm( symTable.getAddress(symbol) )
                # new variable label
                else:
                    addr = symTable.newVar( symbol )
                    bits = code.ainstr_imm( addr )
        
        if instrType is Parser.C_INSTRUCTION:
            dest = parser.dest()
            jump = parser.jump()
            comp = parser.comp()
            # 111 is described in Hack language specification
            # first 1 means c-instr, the other is un-used two bits
            bits = "111" + code.comp( comp ) + code.dest( dest ) + code.jump( jump )

        parser.advance()

        # skip append bits fro L_instr(pseudo instr)
        if instrType is not Parser.L_INSTRUCTION:
            assert len(bits) == 16, "Bits not in basic 16-bit format"
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