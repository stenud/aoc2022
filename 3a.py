f = open("./input/3.txt", "r")

sum_priorities = 0

for i in f:
    bag = i.strip()
    comp1 = bag[:len(bag)//2]
    comp2 = bag[len(bag)//2:]

    found_items = []

    for item in comp1:
        if (comp2.find(item) >= 0) & (found_items.count(item) == 0):
            found_items.append(item)
            if item.islower():
                sum_priorities += ord(item) - 96
            else:
                sum_priorities += ord(item) - 38

print(f"sum of priority values: {sum_priorities}")

f.close()