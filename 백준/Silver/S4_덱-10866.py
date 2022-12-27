from collections import deque
import sys

input = sys.stdin.readline

deq = deque()

for _ in range(int(input())):
    command = input()
    if 'push_front' in command:
        deq.appendleft(command.split()[1])
    elif 'push_back' in command:
        deq.append(command.split()[1])
    elif 'pop_front' in command:
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif 'pop_back' in command:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif 'size' in command:
        print(len(deq))
    elif 'empty' in command:
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif 'back' in command:
        if deq:
            print(deq[-1])
        else:
            print(-1)