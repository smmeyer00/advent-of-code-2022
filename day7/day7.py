class Node:

    def __init__(self, parent, name):
        self.files = [] # sizes of files 
        self.children = [] # sub-folders 
        self.parent = parent 
        self.name = name

    def add_child(self, name):
        for c in self.children:
            if c.name == name:
                return 
        self.children.append(Node(self, name))

    def add_file(self, size, name):
        for f in self.files:
            if f[1] == name:
                return
        self.files.append([size, name])

    def get_child(self, name):
        for c in self.children:
            if c.name == name:
                return c
        return None 



def parse_input(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def folder_size(root):
    size = 0 
    q = [root]

    while len(q) > 0:
        curr = q.pop(0)
        for c in curr.children:
            q.append(c)
        size += sum([i[0] for i in curr.files])
    
    return size 




def p1and2():
    root = Node(None, 'root')
    curr = root 
    lines = parse_input('input.txt')

    for line in lines:
        if line[0] == '$': # command
            args = line.split()
            if args[1] == 'cd':
                if args[2] == '/':
                    curr = root 
                elif args[2] == '..':
                    curr = curr.parent 
                else:
                    curr = curr.get_child(args[2])
        else:
            x, y = line.split()
            if x == 'dir':
                curr.add_child(y)
            else:
                curr.add_file(int(x), y)

    folder_sizes = []
    q = [root]
    while len(q) > 0:
        curr = q.pop(0)
        for c in curr.children:
            q.append(c)
        folder_sizes.append(folder_size(curr))

    ans = 0
    for size in folder_sizes:
        if size <= 100_000:
            ans += size 

    print(f'(P1) Sum of folders lte 100,000: {ans}')

    folder_sizes.sort()
    size_to_delete = 0
    total_used = folder_sizes[-1]
    for size in folder_sizes:
        if 70_000_000 - total_used + size >= 30_000_000:
            size_to_delete = size
            break 

    print(f'(P2) Size of folder to delete: {size_to_delete}')





    

if __name__ == '__main__':
    p1and2()
