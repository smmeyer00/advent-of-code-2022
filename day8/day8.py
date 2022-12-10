

def parse_input(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            grid.append([int(n) for n in line.strip()])

    return grid 



def is_visible(grid, row, col):
    if row == 0 or row == len(grid)-1 or col == 0 or col == len(grid[0])-1:
        return True 

    up, down, left, right = True, True, True, True

    # up
    for r in range(row):
        if grid[r][col] >= grid[row][col]:
            up = False  

    # down
    for r in range(row+1, len(grid)):
        if grid[r][col] >= grid[row][col]:
            down = False  

    # left
    for c in range(col):
        if grid[row][c] >= grid[row][col]:
            left = False  

    # right 
    for c in range(col+1, len(grid[0])):
        if grid[row][c] >= grid[row][col]:
            right = False 

    return up or down or left or right  



def scenic_score(grid, row, col):
    up, down, left, right = 0, 0, 0, 0

    # up 
    crow = row-1 
    while crow >= 0:
        up += 1
        if grid[crow][col] >= grid[row][col]:
            break 
        crow -= 1 

    # down 
    crow = row+1 
    while crow < len(grid):
        down += 1
        if grid[crow][col] >= grid[row][col]:
            break 
        crow += 1 

    
    # left
    ccol = col-1 
    while ccol >= 0:
        left += 1
        if grid[row][ccol] >= grid[row][col]:
            break 
        ccol -= 1 

    
    # right
    ccol = col+1
    while ccol < len(grid[0]):
        right += 1 
        if grid[row][ccol] >= grid[row][col]:
            break 
        ccol += 1

    return up * down * left * right
    





def p1():
    grid = parse_input('input.txt')
    visible = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_visible(grid, row, col):
                visible += 1 

    print(f'(P1) Visible trees: {visible}')
    


def p2():
    grid = parse_input('input.txt')
    max_score = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            s = scenic_score(grid, row, col)
            if s > max_score:
                max_score = s 

    print(f'(P2) Maximum scenic score is: {max_score}')
    


if __name__ == '__main__':
    p1()
    p2()