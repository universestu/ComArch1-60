import sys

NUMMEMORY = 65536 # maximum number of words in memory
NUMREGS = 8 # number of machine registers
MAXLINELENGTH = 1000
halt = 0 # process run or stop
count = 0 # instruction count

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

def convertToBinary(n): #convert int Decimal to String Binary
    if n >= 0:
        return str("{0:025b}".format(n))
    else:
        return str("{0:25b}".format((~(int("{0:24b}".format(abs(n)))) + 0b1) & 0x1ffffff))

def twosComplement(c,f,l): #convert String 2's complement to int Decimal
	if c[f:f+1] == "1": # check sign bit
		return (int(c[f+1:l],2))-pow(2,l-f-1)
	else:
		return int(c[f+1:l],2)

def process(c,s): #check opcode and select fucntion
    global count
    printState(s)
    print ("count : " ,count)
    count += 1
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
        halt(count,s)
    # if opcode is noop (111) do nothing

def add(c,s):
    regA = int(c[3:6],2) #set regA
    regB = int(c[6:9],2) #set regB
    destReg = int(c[22:25],2) #set destReg
    s.reg[destReg] = s.reg[regA] + s.reg[regB]
    #store add value of register
    #at address A and B to register address at destReg
    s.pc += 1 #next instruction

def nand(c,s):
    regA = int(c[3:6],2) #set regA
    regB = int(c[6:9],2) #set regB
    destReg = int(c[22:25],2) #set destReg
    s.reg[destReg] = ~(s.reg[regA] & s.reg[regB])
    #store nand value of register
    #at address A and B to register address at destReg
    s.pc += 1 #next instruction

def lw(c,s):
    regA = int(c[3:6],2) #set regA
    regB = int(c[6:9],2) #set regB
    offsetField = twosComplement(c,9,25) #set offsetField
    s.reg[regB] = s.mem[s.reg[regA]+offsetField]
    #load value from memory address at regA + offsetField
    #to register address at regB
    s.pc += 1 #next instruction

def sw(c,s):
    regA = int(c[3:6],2) #set regA
    regB = int(c[6:9],2) #set regB
    offsetField = twosComplement(c,9,25) #set offsetField
    s.mem[s.reg[regA]+offsetField] = s.reg[regB]
    #store value from register address at regB
    #to memory address at regA + offsetField
    s.pc += 1 #next instruction

def beq(c,s):
    regA = int(c[3:6],2) #set regA
    regB = int(c[6:9],2) #set regB
    offsetField = twosComplement(c,9,25) #set offsetField
    if s.reg[regA] == s.reg[regB]:
    #check value of register A = value of register B
        s.pc = s.pc + 1 + offsetField #branch instruction
    else:
        s.pc += 1 #next instruction

def jalr(c,s):
    regA = int(c[3:6],2) #set regA
    regB = int(c[6:9],2) #set regB
    if regA != regB:
    #check value of register A != value of register B
        s.reg[regB] = s.pc + 1
        #store next instruction to register B
        s.pc = s.reg[regA]
        #branch instruction
    else:
        s.reg[regB] = s.pc + 1 #store next instruction to register B
        s.pc += 1 #next instruction

def halt(cnt,s):
    global halt
    s.pc += 1 #next instruction
    print ("machine halted")
    print ("total of ",cnt," instructions executed.")
    print ("final state of machine:")
    printState(s)
    halt = 1 #stop process

def main():
    state = stateStruct()
    global halt
    with open(sys.argv[1], 'r') as f: #open file
        try:
            for line in f:
                state.mem[state.numMemory] = int(line) #store instruction into mem
                state.numMemory += 1
        except IOError:
            print ("error: usage:",sys.argv[1],"<machine-code file>\n".format(e.errno, e.strerror))
    while halt != 1: #loop until halt
        process (convertToBinary(state.mem[state.pc]),state)

main()
