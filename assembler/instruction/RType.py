RInst = {'add':'000', 'nand':'001'}
fields = 3

def isR(inst):
    return inst in RInst

def convert(inst,symbolic):
    result = '0000000' #31-25
    result += RInst[inst[2]] #24-22
    result += "{0:b}".__format__(inst[3]) #21-19
    result += "{0:b}".__format__(inst[4]) #18-16
    result += '0000000000000'
    result += "{0:b}".__format__(inst[5]) #2-0
    return result
