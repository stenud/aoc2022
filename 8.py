f = open("./input/8.txt", "r")

lines = f.readlines()
f.close()

forest_width =len(lines[0].strip())
forest_height = len(lines)
forest = [[0 for x in range(forest_width)] for x in range(forest_height)] # create empty matrix of right size

def check_dir(dir, x, y, tree):
    match dir:
        case "up":
            for i in range(y):
                if forest[i][x] >= tree:
                    return False
        case "down":
            for i in range(y+1, forest_height):
                if forest[i][x] >= tree:
                    return False
        case "left":
            for i in range(x):
                if forest[y][i] >= tree:
                    return False
        case "right":
            for i in range(x+1, forest_width):
                if forest[y][i] >= tree:
                    return False
    return True

def is_visable(x, y, tree):
    if (x == 0) | (y == 0) | (x == forest_width - 1) | (y == forest_height - 1):
        return 1
    else:
        if check_dir("up", x, y, tree):
            return 1
        if check_dir("down", x, y, tree):
            return 1
        if check_dir("left", x, y, tree):
            return 1
        if check_dir("right", x, y, tree):
            return 1
        return 0

for y, line in enumerate(lines):
    line = line.strip()
    for x, tree in enumerate(line):
        forest[y][x] = int(tree)

visable_trees = 0

for y, col in enumerate(forest):
    for x, tree in enumerate(col):
        visable_trees += is_visable(x, y, tree)

print(f"a: {visable_trees}")
        

