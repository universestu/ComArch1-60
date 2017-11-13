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

def printState(p): #print the state
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

def convertToBinary(n): #convert Decimal to Binary
    if n >= 0:
        return str("{0:025b}".format(n))
    else:
        return str("{0:25b}".format((~(int("{0:24b}".format(abs(n)))) + 0b1) & 0x1ffffff))

def twosComplement(c): #convert 2's complement to Decimal
	if c[9:10] == "1":
		return (int(c[10:25],2))-32768
	else:
		return int(c[10:25],2)

def process(c,s): #check opcode and select fucntion
    if c[0:3] == "000": #check opcode add
        add(c,s)
    elif c[0:3] == "001": #check opcode nand
        nand(c,s)
    elif c[0:3] == "010": #check opcode load
        lw(c,s)
    elif c[0:3] == "011": #check opcode store
        sw(c,s)
    elif c[0:3] == "100": #check opcode branch equal
        beq(c,s)
    elif c[0:3] == "101": #check opcode jump
        jalr(c,s)
    elif c[0:3] == "110": #check opcode halt
        halt(c,s)
    # if opcode is noop do nothing

def add(c,s):
    regA = int(c[4:6],2) #select register at regA
    regB = int(c[7:9],2) #select register at regB
    destReg = int(c[23:25],2) #select register at destReg
    s.reg[destReg] = s.reg[regA] + s.reg[regB] #store add of A and B
    s.pc += 1 #next instruction

def nand(c,s):
    regA = int(c[4:6],2)
    regB = int(c[7:9],2)
    destReg = int(c[23:25],2)
    s.reg[destReg] = ~(s.reg[regA] & s.reg[regB])
    s.pc += 1

def lw(c,s):
    regA = int(c[4:6],2)
    regB = int(c[7:9],2)
    offsetField = twosComplement(c) #convert 2's complement string to decimal
    s.reg[regB] = s.mem[s.reg[regA]+offsetField]
    s.pc += 1

def sw(c,s):
    regA = int(c[4:6],2)
    regB = int(c[7:9],2)
    offsetField = twosComplement(c)
    s.mem[s.reg[regA]+offsetField] = s.reg[regB]
    s.pc += 1

def beq(c,s):
    regA = int(c[4:6],2)
    regB = int(c[7:9],2)
    offsetField = twosComplement(c)
    if s.reg[regA] == s.reg[regB]:
        s.pc = s.pc + 1 + offsetField
    else:
        s.pc += 1


def jalr(c,s):
    regA = int(c[4:6],2)
    regB = int(c[7:9],2)
    if regA != regB:
        s.reg[regB] = s.pc + 1
        s.pc = s.reg[regA]
    else:
        s.reg[regB] = s.pc + 1
        s.pc = s.pc + 1

def halt(c,s):
    s.pc += 1


def main():
    state = stateStruct()
    count = 1
    i = 0
    with open(sys.argv[1], 'r') as f: #open file
        try:
            for line in f:
                state.mem[state.numMemory] = int(line) #store instruction into mem
                state.numMemory += 1
        except IOError:
            print ("error: usage:",sys.argv[1],"<machine-code file>\n".format(e.errno, e.strerror))
    printState(state)
    while i != 1:
        process (convertToBinary(state.mem[state.pc]),state)
        printState(state)
        count += 1
        if convertToBinary(state.mem[state.pc])[0:3] == "110":
            i = 1
    print ("machine halted")
    print ("total of ",count," instructions executed.")
    print ("final state of machine:")
    printState(state)

main()
