from collections import deque
import sys

queue = deque()

n = int(sys.stdin.readline())

while True:
    p = int(sys.stdin.readline())
    if p == -1:
        break
    if p != 0 and len(queue) < n:
        queue.append(p)
    elif queue and p == 0:
        queue.popleft()
     
if queue:            
    print(*queue)  
else:
    print('empty')