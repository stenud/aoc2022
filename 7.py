from anytree import Node, search
f = open("./input/7.txt", "r")

cwd = None
root = Node("root")
dirs_matching_a = []
dirs_matching_b = []

terminal = f.readlines()
for index, item in enumerate(terminal):
    terminal[index] = item.strip()

f.close()

def cd(argument):
    if argument == '/':
        return root
    elif argument == '..':
        return cwd.parent
    else:
        return search.find_by_attr(cwd, argument, maxlevel=2)

def create_dir(foldername):
    if search.find_by_attr(cwd, foldername, maxlevel=2) == None:
        Node(foldername, parent=cwd, size=None)

def create_file(fileinfo):
    size, name = fileinfo.split(' ')
    size = int(size)

    for node in cwd.children:
        if ((node.name == name) & (node.size != None)):
            return 0
    Node(name, parent=cwd, size=size)

def check_dir_total_size(dir):
    sum = 0
    for node in dir.leaves:
        if node.size != None:
            sum += node.size
    return sum

def next_dir_to_check(dir):
    size = check_dir_total_size(dir)
    if size <= 100000:
        dirs_matching_a.append(size)
    if size >= 30_000_000 - available_space:
        dirs_matching_b.append(size)
    for node in dir.children:
        if not node.is_leaf:
            next_dir_to_check(node)

for line in terminal:
    if line.startswith("$ cd "):
        cwd = cd(line[5:])
    elif line.startswith("$ ls"):
        pass # do nothing
    elif line.startswith("dir "):
        create_dir(line[4:])
    else: # files
        create_file(line)

available_space = 70_000_000 - check_dir_total_size(root)
print(available_space)

next_dir_to_check(root)
print(f"a: {sum(dirs_matching_a)}")

dirs_matching_b.sort()
print(f"b: {dirs_matching_b[0]}")