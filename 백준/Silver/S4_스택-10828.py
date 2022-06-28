import sys

top = []


class Stack:
    def push(X):
        top.append(X)

    def pop():
        if len(top) == 0:
            print(-1)
        else:
            print(top[-1])
            top.pop(-1)

    def size():
        print(len(top))

    def empty():
        if len(top) == 0:
            print(1)
        else:
            print(0)

    def top():
        if len(top) == 0:
            print(-1)
        else:
            print(top[-1])


for _ in range(int(sys.stdin.readline())):
    ex_input = sys.stdin.readline()
    if 'push' in ex_input:
        Stack.push(int(ex_input.split()[1]))
    elif 'pop' in ex_input:
        Stack.pop()
    elif 'size' in ex_input:
        Stack.size()
    elif 'empty' in ex_input:
        Stack.empty()
    elif 'top' in ex_input:
        Stack.top()
