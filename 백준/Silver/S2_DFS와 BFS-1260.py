# 인접 리스트
from collections import deque

n, m, start = map(int, input().split()) # 정점의 개수, 간선의 개수, 시작 정점
a = [[] for _ in range(n + 1)] # 인접 리스트
check = [False] * (n + 1) # 방문 하였는지 확인

for _ in range(m): # 방향 없는 그래프이므로, 인접 리스트에 저장
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
    
print('a ===', a)
    
for i in range(1, n + 1): # 인접 리스트의 각 정점들의 요소들을 정렬
    a[i].sort()
    
print('a ===', a)
    
def dfs(x):
    print('======================dfs======================')
    global check
    check[x] = True # 인자로 받아 왔다는 것은 방문했다는 뜻이므로 True
    print('check ===', check)
    print(x, end=' ') # 방문하였으므로 출력
    
    for y in a[x]: # 인접 리스트에 저장되어 있는, x라는 정점에 맞닿아 있는 정점들을 불러옴.
        print('a ===', a)
        print('a[x], y ===', a[x], y)
        print('check ===', check)
        if check[y] == False: # 해당 정점에 방문하지 않았다면,
            dfs(y) # dfs의 인자로 y라는 정점을 넣어줌.
            
def bfs(start):
    print('======================bfs======================')
    check = [False] * (n + 1) # dfs에서 check를 사용하였으므로, 변수를 새로 선언.
    q = deque()
    q.append(start) # 큐에 시작하는 첫 정점을 넣어줌.
    check[start] = True # 마찬가지로 방문하였으므로 방문 처리
    print('check ===', check)
    
    while q: # 큐가 empty가 아닐 때
        print('q ===', q)
        x = q.popleft() # 방문한 정점
        print(x, end=' ') # 방문한 정점이므로 출력
        
        for y in a[x]: # 인접 리스트에 저장되어 있는, x라는 정점에 맞닿아 있는 정점들을 불러옴.
            print('a ===', a)
            print('a[x], y ===', a[x], y)
            print('check ===', check)
            if check[y] == False: # 해당 정점에 방문하지 않았다면,
                check[y] = True # 해당 정점을 방문 처리한 후,
                q.append(y) # 큐에 추가한다.
                print('q ===', q)
                
dfs(start)
print()
bfs(start)
print()



'''
# 간선 리스트

from collections import deque

n, m, start = map(int, input().split())
edges = []
check = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    edges.append((v, u))
    
m *= 2
edges.sort()
cnt = [0] * (n + 1)

for u, v in edges:
    cnt[u] += 1

for i in range(1, n + 1):
    cnt[i] += cnt[i - 1]

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for i in range(cnt[x - 1], cnt[x]):
        y = edges[i][1]
        if check[y] == False:
            dfs(y)

def bfs(start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(cnt[x - 1], cnt[x]):
            y = edges[i][1]
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()

'''



'''
# DFS 비재귀 구현 1

from collections import deque

n, m, start = map(int, input().split())
a = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
    
for i in range(1, n + 1):
    a[i].sort()

def dfs(node):
    check = [False] * (n + 1)
    stack = []
    stack.append((node, 0))
    check[node] = True
    print(node, end=' ')
    while stack:
        x, start = stack.pop()
        for i in range(start, len(a[x])):
            y = a[x][i]
            if check[y] == False:
                print(y, end=' ')
                check[y] = True
                stack.append((x, i + 1))
                stack.append((y, 0))
                break

def bfs(start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()

'''



'''
# DFS 비재귀 구현 2

from collections import deque

def dfs(n, a, node):
    check = [False] * (n + 1)
    start = [0] * (n + 1)
    stack = []
    stack.append(node)
    check[node] = True
    print(node, end=' ')
    while stack:
        node = stack.pop()
        while start[node] < len(a[node]):
            nxt = a[node][start[node]]
            if check[nxt] == False:
                print(nxt, end=' ')
                check[nxt] = True
                stack.append(node)
                stack.append(nxt)
                break
            start[node] += 1

def bfs(n, a, start):
    q = deque()
    check = [False] * (n + 1)
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)

n, m, start = map(int, input().split())
a = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
    
for i in range(1, n + 1):
    a[i].sort()
    
dfs(n, a, start)
print()
bfs(n, a, start)
print()

'''