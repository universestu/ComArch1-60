OInst = {'halt':'110', 'noop':'111'}
fields = 0

def isO(inst):
    return inst in OInst

def convert(inst):
    print(inst)