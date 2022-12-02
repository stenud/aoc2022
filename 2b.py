f = open("./input/2.txt", "r")

score = 0

for i in f:
    game = i.strip().split(' ')

    if game[1] == 'X':
        match game[0]:
            case 'A':
                score += 3
            case 'B':
                score += 1
            case 'C':
                score += 2
    elif game[1] == 'Y':
        match game[0]:
            case 'A':
                score += 4
            case 'B':
                score += 5
            case 'C':
                score += 6
    elif game[1] == 'Z':
        match game[0]:
            case 'A':
                score += 8
            case 'B':
                score += 9
            case 'C':
                score += 7

print(score)