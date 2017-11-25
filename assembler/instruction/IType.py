IInst = {'lw':'010', 'sw':'011', 'beq':'100'}           # Declare available instruction
fields = 3
regA = ''
regB = ''
offsetField = ''

def isI(inst):                                          # I-Type check
    return inst in IInst

def setFields(inst,symbolic):                           # Set I-Type fields
    global regA
    global regB
    global offsetField
    regA = "{0:03b}".format(int(inst[3]))               # Convert field 1 to binary
    regB = "{0:03b}".format(int(inst[4]))               # Convert field 2 to binary
    try:
        offsetField = int(inst[5])
    except ValueError:                                  # Offset is symbolic
        if inst[5] in symbolic:
            offsetField = int(symbolic[inst[5]])
            if inst[2] == 'beq':                        # Calculate target offset for 'beq'
                offsetField = branchAddress(inst, offsetField)
        else:
            print("\""+ inst[5] +"\" Label undefined")  # Exception undefined label
            exit(1)

    if -32768 <= offsetField <= 32767:                  # Convert offset to binary
        offsetField = format(offsetField if offsetField >= 0 else (1 << 16) + offsetField, '016b')
    else:
        print('OffsetField out of range')               # Offset over 16-bit
        exit(1)

def branchAddress(inst,target):                         #  'beq' offset calculator
    return target - (inst[0]+1)

def convert(inst,symbolic):                             # Assemble each part
    setFields(inst,symbolic)
    result = format(0, '07') #31-25
    result += IInst[inst[2]][-3:] #24-22
    result += regA[-3:] #21-19
    result += regB[-3:] #18-16'
    result += offsetField[-16:] #15-0
    return result
