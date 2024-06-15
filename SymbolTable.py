class SymbolTable:
    def __init__(self):
        self.table = {}
        # custom var in hack start at 16, continues increment
        self.varAddrCounter = 16
    
    def addEntry(self, symbol: str, address: int):
        self.table[ symbol ] = address
    
    def contains(self, symbol: str):
        return symbol in self.table;
    
    def getAddress(self, symbol: str):
        assert self.contains(symbol), "Try to get a undefined symbol in SymbolTable, something must went wrong."

        addr = self.table[ symbol ]
        assert isinstance(addr, int), "Addr is not integer, something wrong."  

        return addr
    
    def newVar(self, symbol):
        assert not self.contains(symbol), "try to add a already defined variable"
        addr = self.varAddrCounter
        self.addEntry( symbol, addr )
        self.varAddrCounter += 1
        return addr
