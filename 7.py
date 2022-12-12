from anytree import Node, search
f = open("./input/7.txt", "r")

cwd = None
root = Node("root")
dirs_matching_a = []

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
        Node(foldername, parent=cwd)

def create_file(fileinfo):
    size, name = fileinfo.split(' ')
    size = int(size)
    if search.find_by_attr(cwd, name, maxlevel=2) == None:
        Node(name, parent=cwd, size=size)

def check_dir_total_size(dir):
    sum = 0
    for node in dir.leaves:
        sum += node.size
    return sum

def next_dir_to_check(dir):
    size = check_dir_total_size(dir)
    if size <= 100000:
        dirs_matching_a.append(size)
    for node in dir.children:
        if node.is_leaf == False:
            next_dir_to_check(node)

for line in terminal: # TODO.TEST: change when ready
    if line.startswith("$ cd "):
        cwd = cd(line[5:])
    elif line.startswith("$ ls"):
        pass # do nothing
    elif line.startswith("dir "):
        create_dir(line[4:])
    else: # files
        create_file(line)

next_dir_to_check(root)

print(f"a: {sum(dirs_matching_a)}")
