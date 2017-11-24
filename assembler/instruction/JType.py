JInst = {'jalr':'101'}                      # Declare available instruction
fields = 2
regA = ''
regB = ''

def isJ(inst):                              # J-Type check
    return inst in JInst

def setFields(inst):                        # Set I-Type fields
    global regA
    global regB
    regA = "{0:03b}".format(int(inst[3]))   # Convert field 1 to binary
    regB = "{0:03b}".format(int(inst[4]))   # Convert field 2 to binary

def convert(inst,symbolic):                 # Assemble each part
    setFields(inst)
    result = format(0, '07') #31-25
    result += JInst[inst[2]][-3:] #24-22
    result += regA[-3:] #21-19
    result += regB[-3:] #18-16
    result += format(0, '016') #15-0
    return result