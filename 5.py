from copy import deepcopy

f = open("./input/5.txt", "r")

stacks = [[],[],[],[],[],[],[],[],[]]
lines = f.readlines()
f.close()

def get_message():
    message = ""
    for stack in stacks:
        message += stack[-1]
    return message

def move_crates(instruction):
    for i in range(instruction[0]):
        stacks[instruction[2]].append(stacks[instruction[1]][-1])
        stacks[instruction[1]].pop()

def move_crates_b(instruction):
    stacks[instruction[2]] += stacks[instruction[1]][-instruction[0]:]
    stacks[instruction[1]] = stacks[instruction[1]][:-instruction[0]]

def process_instruction(line):
    instr = line.strip().split(' ')
    nums = (int(instr[1]), int(instr[3])-1, int(instr[5])-1)
    return nums

def solve_a():
    for line in lines:
        move_crates(process_instruction(line))

    print(f"message in a: {get_message()}")

def solve_b():
    for line in lines:
        move_crates_b(process_instruction(line))

    print(f"message in b: {get_message()}")

for i in range(8):
    for j, c in enumerate(lines[i]):
        if c.isalpha():
            stacks[(j-1)//4].insert(0, c)

start_stacks = deepcopy(stacks)
lines = lines[10:]

solve_a()

stacks = deepcopy(start_stacks)
solve_b()
