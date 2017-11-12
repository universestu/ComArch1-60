IInst = {'lw':'010', 'sw':'011', 'beq':'100'}
fields = 3
regA = ''
regB = ''
offsetField = ''

def isI(inst):
    return inst in IInst

def setFields(inst,symbolic):
    global regA
    global regB
    global offsetField
    regA = "{0:03b}".format(int(inst[3]))
    regB = "{0:03b}".format(int(inst[4]))
    try:
        offsetField = int(inst[5])
    except ValueError:
        if inst[5] in symbolic:
            offsetField = int(symbolic[inst[5]])
        else:
            print("Label undefined")
            exit(1)

    if -32768 <= offsetField <= 32767:
        offsetField = format(offsetField if offsetField >= 0 else (1 << 16) + offsetField, '016b')
    else:
        print('OffsetField out of range')
        exit(1)

def convert(inst,symbolic):
    setFields(inst,symbolic)
    result = format(0, '07') #31-25
    result += IInst[inst[2]] #24-22
    result += regA #21-19
    result += regB #18-16'
    result += offsetField #15-0
    return result
