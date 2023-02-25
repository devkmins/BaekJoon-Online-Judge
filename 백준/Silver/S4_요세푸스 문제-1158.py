from collections import deque

n, m = map(int,input().split())

q = deque(range(1, n + 1))

ans = []

for i in range(n - 1):
    for j in range(m - 1):
        q.append(q.popleft())
    ans += [q.popleft()]
    print(ans)

ans += [q[0]]

print('<' + ', '.join(map(str, ans)) + '>')