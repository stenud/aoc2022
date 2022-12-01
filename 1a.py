f = open("./input/1.txt", "r")

lines = []
sum = 0

for i in f:
    if i != '\n':
        sum += int(i)
    else:
        lines.append(int(sum))
        sum = 0

lines.append(int(sum)) #last elf

f.close()

lines.sort()

print(lines)
print(lines[-1]) #1a
print(lines[-1]+lines[-2]+lines[-3]) #1b