import input

data = input.data
# print(data[10][0:6])

processed_data = []
tmp = 0
for head in data:
    processed_data.append([head[0:6].rstrip()])
    for sp in head[7:].split():
        processed_data[tmp].append(sp)
    tmp += 1

for x in processed_data:
    print(x)