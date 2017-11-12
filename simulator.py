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
        self.numMemory = 0

def printState(p):
    i = 0
    print ('\n@@@\nstate:')
    print ("\tpc ", p.pc )
    print ("\tmemory:")
    for i in range(0,p.numMemory):
        print ("\t \tmem[ ",i," ] ", p.mem[i])
    print ("\tregisters:")
    for i in range(0,NUMREGS):
        print ("\t \treg[ ",i," ] " , p.reg[i])
    print ("end state")

def convertToBinary(n):
    if n >= 1:
        return str("{0:025b}".format(n))
    else:
        return str("{0:25b}".format((~(int("{0:24b}".format(abs(n)))) + 0b1) & 0x1ffffff))

def process(c,s):
    if c[0:3] == "000":
        add(c,s)
    # elif c[0:3] == "001":
    #     nand(c,s)
    # elif c[0:3] == "010":
    #     lw(c,s)
    # elif c[0:3] == "011":
    #     sw(c,s)
    # elif c[0:3] == "100":
    #     beq(c,s)
    # elif c[0:3] == "101":
    #     jalr(c,s)
    # elif c[0:3] == "110":
    #     halt(c,s)
    # else:
    #     noop(c,s)

def add(c,s):
    regA = int(c[4:6],2)
    regB = int(c[7:9],2)
    destReg = int(c[23:25],2)
    s.reg[destReg] = s.reg[regA] + s.reg[regB]


def main():
    state = stateStruct()
    state.reg[1] = 2
    state.reg[2] = 3
    with open(sys.argv[1], 'r') as f:
        try:
            for line in f:
                process (convertToBinary(int(line)),state)
        except IOError:
            print ("error: usage:",sys.argv[1],"<machine-code file>\n".format(e.errno, e.strerror))
        printState(state)

main()
