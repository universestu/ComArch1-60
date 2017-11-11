IInst = {'lw':'010', 'sw':'011', 'beq':'100'}
fields = 3

def isI(inst):
    return inst in IInst

def convert(inst):
    print(inst)