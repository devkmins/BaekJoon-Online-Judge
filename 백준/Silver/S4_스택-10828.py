import sys

n = int(sys.stdin.readline())

top = []

for _ in range(n):
    ex_input = sys.stdin.readline().split()
    if 'push' in ex_input:
        top.append(ex_input[1])
    elif 'pop' in ex_input:
        if len(top) == 0:
            print(-1)
        else:
            print(top[-1])
            top.pop(-1)
    elif 'size' in ex_input:
        print(len(top))
    elif 'empty' in ex_input:
        if len(top) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in ex_input:
        if len(top) == 0:
            print(-1)
        else:
            print(top[-1])