import sys
sys.path.append('instruction')
import JType as J
import IType as I
import OType as O
import RType as R

symbolic = {}
toConvert = []

def seperate(inst):
    if(J.isJ(inst[2])):
        return J.convert(inst,symbolic)
    elif(I.isI(inst[2])):
        return I.convert(inst,symbolic)
    elif(O.isO(inst[2])):
        return O.convert(inst,symbolic)
    elif(R.isR(inst[2])):
        return R.convert(inst,symbolic)
    elif(inst[2] == '.fill'):
        return convert(inst)
    else:
        return 'opcode undefined'

def convert(inst):
    return inst[3]


def setSymbolic(data):
    for e in data:
        if(e[1][0] != '' and e[2] != '.fill'):
            symbolic[e[1][0]] = e[0]
        elif(e[2] == '.fill'):
            if(e[3] in symbolic):
                symbolic[e[1][0]] = symbolic[e[3]]
            else:
                symbolic[e[1][0]] = e[3]