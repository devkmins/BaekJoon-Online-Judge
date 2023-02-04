from collections import deque

queue = deque(range(1, int(input()) + 1))
ans = ''
cnt = 0

while len(queue) > 1:
    if cnt % 2 == 0:
        ans += str(queue.popleft()) + ' '
    else:
        queue.append(queue.popleft())
    cnt += 1
    
ans += str(queue[0])

print(ans)