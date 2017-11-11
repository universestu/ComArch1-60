JInst = {'jalr':'101'}
fields = 2

def isJ(inst):
    return inst in JInst

def convert(inst):
    print(inst)