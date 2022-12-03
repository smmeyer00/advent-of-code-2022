# A, X = rock
# B, Y = paper
# C, Z = scissors


beats = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B',
}

draw = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

# returns score of player who played x
def p1_score(x, y):
    s = 0

    # win/lose/draw points
    if draw[x] == y:
        s += 3
    elif beats[x] == y:
        s += 6

    # selection points
    s += points[x]

    return s


to_beat = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

to_draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

to_lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

def p2_score(x, y):
    if y == 'X':
        # lose
        return points[to_lose[x]]
    elif y == 'Y':
        # draw
        return 3 + points[to_draw[x]] 
    else:
        # win
        return 6 + points[to_beat[x]] 



p1 = 0
p2 = 0
with open('input.txt', 'r') as file:
    for line in file:
        x, y = line.split()
        p1 += p1_score(y, x)
        p2 += p2_score(x, y)

print(f'Total score (p1): {p1}')
print(f'Total score (p2): {p2}')





