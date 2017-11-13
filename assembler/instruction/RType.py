RInst = {'add':'000', 'nand':'001'}
fields = 3
regA = ''
regB = ''
destReg = ''

def isR(inst):
    return inst in RInst

def setFields(inst):
    global regA
    regA = "{0:03b}".format(int(inst[3]))
    global regB
    regB = "{0:03b}".format(int(inst[4]))
    global destReg
    destReg= "{0:03b}".format(int(inst[5]))



def convert(inst,symbolic):
    setFields(inst)
    result = format(0, '07') #31-25
    result += RInst[inst[2]][-3:] #24-22
    result += regA[-3:] #21-19
    result += regB[-3:] #18-16
    result += format(0, '013') #15-3
    result += destReg[-3:] #2-0
    return result
