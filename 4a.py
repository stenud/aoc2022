import re

f = open("./input/4.txt", "r")

count = 0

def compareSections(pair):
    if (pair[0] >= pair[2]) & (pair[1] <= pair[3]):
        return 1
    elif (pair[2] >= pair[0]) & (pair[3] <= pair[1]):
        return 1
    else:
        return 0

for i in f:
    pair = re.split( ',|-', i.strip() )
    pair = [int(x) for x in pair]
    count += compareSections(pair)

print(f"Pairs overlapping: {count}")

f.close()