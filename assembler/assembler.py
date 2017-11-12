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

with open(input.sys.argv[2], 'w') as output_file:
    for x in processed_data:
        try:
            output_file.writelines(str(int(inst.seperate(x), 2))+'\n')
        except TypeError:
            output_file.writelines(str(inst.seperate(x))+'\n')
    output_file.close()
exit(0)