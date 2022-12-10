


# -> [ (amount, from, to) ]
def get_instructions(filename, start_index): 
    r = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(start_index, len(lines)):
            # parse instruction 
            arr = lines[i].split()
            r.append([int(arr[1]), int(arr[3])-1, int(arr[5])-1])

    return r 



def get_stacks(filename):
    stacks = [[] for i in range(9)]
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if [e for e in line.split()] == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                instruction_start = i + 2
                break

            # on line i 
            col = 1
            stack_index = 0
            while col in range(len(line)):
                if line[col] != ' ':
                    stacks[stack_index].append(line[col])   
                col += 4
                stack_index += 1 

    return stacks, instruction_start

            

def parse_input(filename):
    stacks, i_start = get_stacks(filename)
    instructions = get_instructions(filename, i_start)

    return stacks, instructions 



def simulate1(stacks, instruction):
    amount, from_i, to_i = instruction 
    for _ in range(amount):
        stacks[to_i].insert(0, stacks[from_i].pop(0))


def simulate2(stacks, instruction):
    amount, from_i, to_i = instruction
    temp = stacks[from_i][:amount]
    stacks[to_i] = temp + stacks[to_i]
    stacks[from_i] = stacks[from_i][amount:]


def p1():
    stacks, instructions = parse_input('input.txt')
    for e in instructions:
        simulate1(stacks, e)

    res = ''
    for s in stacks:
        res += s[0]

    print(f'(P1) Top of stacks: {res}')


def p2():
    stacks, instructions = parse_input('input.txt')
    for e in instructions:
        simulate2(stacks, e)

    res = ''
    for s in stacks:
        res += s[0]

    print(f'(P2) Top of stacks: {res}')


if __name__ == '__main__':
    p1()
    p2()
