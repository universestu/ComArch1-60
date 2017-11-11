import sys

with open(sys.argv[1], 'r') as input_file:
    data = filter(None, (line.rstrip() for line in input_file))