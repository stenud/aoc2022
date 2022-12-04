f = open("./input/3.txt", "r")

sum_badges = 0

bags = f.readlines()
f.close()

def addBadge(badge):
    global sum_badges
    if badge.islower():
        sum_badges += ord(badge) - 96
    else:
        sum_badges += ord(badge) - 38

for i in range(0, len(bags), 3):
    for item in bags[i]:
        if item =='\n':
            raise ValueError("Not a letter: '\n'")
        if (bags[i+1].find(item) >= 0) & (bags[i+2].find(item) >= 0):
            addBadge(item)
            break

print(f"sum of badge values: {sum_badges}")