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
    result = '0000000' #31-25
    result += RInst[inst[2]] #24-22
    result += regA #21-19
    result += regB #18-16
    result += '0000000000000'
    result += destReg #2-0
    return result
