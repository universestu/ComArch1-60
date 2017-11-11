RInst = {'add':'000', 'nand':'001'}
fields = 3

def isR(inst):
    return inst in RInst

def convert(inst):
    print(inst)