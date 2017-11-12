JInst = {'jalr':'101'}
fields = 2
regA = ''
regB = ''

def isJ(inst):
    return inst in JInst

def setFields(inst):
    global regA
    regA = "{0:03b}".format(int(inst[3]))
    global regB
    regB = "{0:03b}".format(int(inst[4]))

def convert(inst,symbolic):
    setFields(inst)
    result = '0000000' #31-25
    result += JInst[inst[2]] #24-22
    result += regA #21-19
    result += regB #18-16
    result += format(0, '016') #15-0
    return result