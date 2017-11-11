import sys

NUMMEMORY = 65536 # maximum number of words in memory
NUMREGS = 8 # number of machine registers
MAXLINELENGTH = 1000

class stateStruct:
    pc = None
    mem = None
    reg = None
    numMemory = None
    def __init__(self):
        self.pc = 0
        self.mem = [0] * NUMMEMORY
        self.reg = [0] * NUMREGS
        self.numMemory = 8

def printState(p):
    i = 0
    print ('\n@@@\nstate:')
    print ("\tpc ", p.pc )
    print ("\tmemory:")
    for i in range(0,p.numMemory):
        print ("\t \tmem[ ",i," ] ", p.mem[i])
    print ("\tregisters:")
    for i in range(0,NUMREGS):
        print ("\t \treg[ ", i ," ] " , p.reg[i])
    print ("end state")

def main():
    state = stateStruct()
    with open(sys.argv[1], 'r') as f:
        try:
            contents = f.read()
        except IOError:
            print ("error: usage:",sys.argv[1],"<machine-code file>\n".format(e.errno, e.strerror))
    print (contents)
    # printState(state)

main()
