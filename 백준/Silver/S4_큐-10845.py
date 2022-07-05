from queue import Queue
import sys

que = Queue()

N = int(input())

for _ in range(N):
    command = sys.stdin.readline()
    if 'push' in command:
        que.put(command.split()[1])
    elif 'pop' in command:
        if que.empty() == False:
            print(que.get())
        else:
            print(-1)
    elif 'size' in command:
        print(que.qsize())
    elif 'empty' in command:
        if que.empty() == True:
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if que.empty() == True:
            print(-1)
        else:
            print(que.queue[0])
    elif 'back' in command:
        if que.empty() == True:
            print(-1)
        else:
            print(que.queue[-1])