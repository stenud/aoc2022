import re

f = open("./input/4.txt", "r")

count = 0

def compareSections(pair):
    for i in range(pair[0], pair[1]+1):
        if i in range(pair[2], pair[3]+1):
            return 1

    return 0

for i in f:
    pair = re.split( ',|-', i.strip() )
    pair = [int(x) for x in pair]
    count += compareSections(pair)

print(f"Pairs overlapping: {count}")

f.close()