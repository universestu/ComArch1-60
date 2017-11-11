import sys
sys.path.append('instruction')
import JType as J
import IType as I
import OType as O
import RType as R

def seperateInst(inst):
    if(J.isJ(inst[2])):
        J.convert(inst)
    elif(I.isI(inst[2])):
        I.convert(inst)
    elif(O.isO(inst[2])):
        O.convert(inst)
    elif(R.isR(inst[2])):
        R.convert(inst)
    elif(inst[2] == '.fill'):
        fill(inst)
    else:
        print('opcode undefined')


def fill(inst):
    print(inst)