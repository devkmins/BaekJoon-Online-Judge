'''
해결 방법 -
1. 일반적인 큐 문제임.
2. queue 모듈은 thread 등을 잘 처리하기 위해 (문제 풀이에서는 불필요한) 동기화 과정을 거치기 때문에 
collections.deque에 비해 많이 느림.
queue는 멀티스레드 환경을 위한 모듈
'''

from collections import deque
import sys

que = deque([])

N = int(input())

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        que.append(command[1])
    elif command[0] == 'pop':
        if len(que):
            print(que.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        if len(que):
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(que):
            print(que[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(que):
            print(que[-1])
        else:
            print(-1)