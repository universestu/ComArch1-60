OInst = {'halt':'110', 'noop':'111'}        # Declare available instruction
fields = 0

def isO(inst):                              # O-Type check
    return inst in OInst

def convert(inst,symbolic):                 # Assemble each part
    result = format(0, '07') #31-25
    result += OInst[inst[2]][-3:] #24-22
    result += format(0, '022') #21-0
    return result