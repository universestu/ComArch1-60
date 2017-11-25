import input
import instruction as inst

data = input.data                                       # Input file to Data memory

processed_data = []                                     # Processed input Data memory
tmp = 0
for head in data:
    processed_data.append([tmp])                        # Append Number of line
    processed_data[tmp].append([head[0:6].rstrip()])    # Append label
    for sp in head[7:].split():                         # Append fileds and comment part
        processed_data[tmp].append(sp)
    tmp += 1

inst.setSymbolic(processed_data)                        # Set Symbolic memory

with open(input.sys.argv[1].split('.')[0] + '-out.asm', 'w') as output_file:
    for x in processed_data:
        try:
            if('-b' in input.sys.argv):                                     # Write output in binary mode
                output_file.writelines(str(inst.seperate(x))  +'\n')
            else:
                output_file.writelines(str(int(inst.seperate(x), 2))+'\n')  # Write output in decimal mode
        except TypeError:
            output_file.writelines(str(inst.seperate(x)) +'\n')             # Write .fill part
    output_file.close()
exit(0)