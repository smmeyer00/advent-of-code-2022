def parse_input(filename):
    l = []
    with open(filename, 'r') as file:
        for line in file:
            line.strip()
            p1, p2 = line.split(',')
            x1, y1 = [int(i) for i in p1.split('-')]
            x2, y2 = [int(i) for i in p2.split('-')]
            l.append([ [x1, y1], [x2, y2] ])
        return l 


def fully_overlaps(pair):
    x1, y1 = pair[0]
    x2, y2 = pair[1]

    # if second range is smaller, swap
    if y2 - x2 < y1 - x1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1 

    if y1 <= y2 and x1 >= x2:
        return True 
    return False 
    

def overlaps(pair):
    x1, y1 = pair[0]
    x2, y2 = pair[1]

    if (x1 <= y2 and x1 >= x2) or (y1 <= y2 and y1 >= x2) or (x2 <= y1 and x2 >= x1) or (y2 <= y1 and y2 >= x1):
        return True 
    return False 


def p1():
    range_pairs = parse_input('input.txt')
    total_overlaps = 0
    for pair in range_pairs:
        if fully_overlaps(pair):
            total_overlaps += 1
    print(f'(P1) Total fully covered overlaps: {total_overlaps}')


def p2():
    range_pairs = parse_input('input.txt')
    total_overlaps = 0
    for pair in range_pairs:
        if overlaps(pair):
            total_overlaps += 1
    print(f'(P2) Total overlaps: {total_overlaps}')


if __name__ == '__main__':
    p1()
    p2()

    