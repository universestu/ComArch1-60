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
    # print(head,tmp)

# for x in processed_data:
#     print(x)

inst.setSymbolic(processed_data)
print(inst.symbolic)