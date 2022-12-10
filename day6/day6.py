
def parse_input(filename):
    with open(filename, 'r') as file:
        return file.readline().strip()



def data_start_index(stream):
    last4 = []
    for i, c in enumerate(stream):
        last4.append(c)
        if len(last4) > 4:
            last4.pop(0)
        if len(set(last4)) == 4:
            return i+1


def message_start_index(stream):
    last14 = []
    for i, c in enumerate(stream):
        last14.append(c)
        if len(last14) > 14:
            last14.pop(0)
        if len(set(last14)) == 14:
            return i+1
        

def p1():
    stream = parse_input('input.txt')
    data_start = data_start_index(stream)
    print(f'(P1) Start of data: {data_start}')


def p2():
    stream = parse_input('input.txt')
    msg_start = message_start_index(stream)
    print(f'(P2) Start of data: {msg_start}')


if __name__ == '__main__':
    p1()
    p2()

