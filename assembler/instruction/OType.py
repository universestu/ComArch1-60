OInst = {'halt':'110', 'noop':'111'}
fields = 0

def isO(inst):
    return inst in OInst

def convert(inst,symbolic):
    result = format(0, '07') #31-25
    result += OInst[inst[2]][-3:] #24-22
    result += format(0, '022') #21-0
    return result