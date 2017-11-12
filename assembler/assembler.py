import input
import instruction as inst

data = input.data

processed_data = []
tmp = 0
for head in data:
    processed_data.append([tmp])
    processed_data[tmp].append([head[0:6].rstrip()])
    for sp in head[7:].split():
        processed_data[tmp].append(sp)
    tmp += 1

inst.setSymbolic(processed_data)
for x in processed_data:
    # print(inst.seperate(x))
    try:
        print( int(inst.seperate(x), 2) )
    except TypeError:
        print(inst.seperate(x))
    # print(x)

# for x in inst.symbolic:
#     print(x, inst.symbolic[x])



# print(inst.seperate(processed_data[2]), len(inst.seperate(processed_data[2])))
# print(inst.symbolic)