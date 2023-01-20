import sys

sys.setrecursionlimit(10 ** 9)

n, m, start = map(int, input().split())
a = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    a[u].append(v)
    a[v].append(u)
    
def dfs(x):
    global cnt
    check[x] = cnt
    a[x].sort(reverse=True)
    
    for y in a[x]:
        if check[y] == False:
            cnt += 1
            dfs(y)
            
dfs(start)

for i in range(1, n + 1):
    print(check[i])