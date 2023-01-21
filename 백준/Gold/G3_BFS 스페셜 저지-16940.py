from collections import deque

n = int(input())
a = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)

order = list(map(int, input().split())) # BFS 방문 순서
order = [x - 1 for x in order] # 각각 인덱스 - 1

check = [False] * n
parent = [-1] * n # 인접 리스트에서 1 안에 2, 3이 있으면 2, 3의 부모는 1
q = deque()

q.append(0)
check[0] = True
m = 1 # 큐의 크기

for i in range(n):
    if not q: # BFS가 진행 중인데 큐가 비어 있는 경우
        print(0)
        exit()
    
    x = q.popleft()
    if x != order[i]: # 순서가 올바르지 않은 경우
        print(0)
        exit()

    cnt = 0
    for y in a[x]:
        if check[y] == False: # 방문하지 않은 경우
            parent[y] = x # y의 부모는 x임을 지정
            cnt += 1

    for j in range(cnt):
        if m + j >= n or parent[order[m + j]] != x: # x와 연결되지 않은 정점이 큐에 들어가 있는 경우
            print(0)
            exit()
        q.append(order[m + j]) 
        check[order[m + j]] = True
    m += cnt
    
print(1)