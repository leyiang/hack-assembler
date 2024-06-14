import sys
import Parser

if len(sys.argv) < 2:
    print("Usage: \n\tpython main.py <asm file path>")
    exit()

parser = Parser.Parser( sys.argv[1] )
file = parser.file

while parser.hasMoreLines():
    print( parser.line )
    parser.advance()