priority = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def find_common_item(rucksack):
    left_half = rucksack[:int(len(rucksack)/2)]
    right_half = rucksack[int(len(rucksack)/2):]

    for c in left_half:
        if c in right_half:
            return c


def p1():
    score = 0
    with open('input.txt', 'r') as file:
        for line in file:
            common = find_common_item(line.strip())
            score += priority.index(common)

    print(f'(P1) Score is {score}')


def p2():
    score = 0
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]
    
    while len(lines) > 0:
        r1 = lines.pop()
        r2 = lines.pop()
        r3 = lines.pop()

        for c in r1:
            if c in r2 and c in r3:
                score += priority.index(c)
                break 

    print(f'(P2) Score is {score}')


p2()