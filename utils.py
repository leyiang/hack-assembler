from termcolor import colored

def log( *args ):
    for c in args:
        print( colored(c, "red") )