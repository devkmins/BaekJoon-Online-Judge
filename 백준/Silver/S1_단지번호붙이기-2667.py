# BFS

from collections import deque, Counter
# Counter 클래스는 iterable의 원소의 개수를 셀 떄 편리하게 사용할 수 있는 기능임. dict와 비슷함.
from functools import reduce
# reduce() 함수는 여러 개의 데이터를 대상으로 주로 누적 집계를 내기 위해서 사용함.
# 기본적으로 초기값을 기준으로 데이터를 루프 돌면서 집계 합수를 계속해서 적용하면서 데이터를 누적하는 방식으로 작동함.
# reduce(집계 함수, 순회 가능한 데이터[, 초기값])

dx = [0, 0, 1, -1] # x행의 방향(우 좌 하 상)
dy = [1, -1, 0, 0] # y열의 방향(우 좌 하 상)

def bfs(x, y, cnt):
    q = deque()
    q.append((x, y)) # x행 y열을 큐에 저장
    group[x][y] = cnt # n x n 크기의 지도의 x행 y열에 cnt(단지 번호) 저장
    
    while q:
        x, y = q.popleft()
        for k in range(4): # (0, 1, 2, 3) -> (상, 하, 좌, 우)
            nx, ny = x + dx[k], y + dy[k] 
            if 0 <= nx < n and 0 <= ny < n: # n x n 크기의 지도 안에 있을 떄
                if a[nx][ny] == 1 and group[nx][ny] == 0: # nx행, ny열에 집이 있는데, 방문한 적이 없다면,
                    q.append((nx, ny)) # 큐에 nx행, ny열을 push
                    group[nx][ny] = cnt # 지도의 nx행 ny열에 cnt(단지 번호) 저장
                    
n = int(input()) # 지도의 크기, n x n
a = [list(map(int, list(input()))) for _ in range(n)] # 행렬, 입력 받은 지도를 저장함.
group = [[0] * n for _ in range(n)] # 지도를 만들어, 체크해 주는 부분
cnt = 0 # 단지 번호

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0: # 집이 있는데, 방문한 적이 없다면,
            cnt += 1 # 단지 번호 + 1
            bfs(i, j, cnt) # x행, y열, cnt(단지 번호)

print(group)            
ans = reduce(lambda x, y: x + y, group) # 2차원 리스트인 group 내에 있는 요소들을 1차원 리스트로 만들어 줌.
print(ans)
ans = [x for x in ans if x > 0] # 0보다 큰 경우에만 ans에 저장
print(ans)
print(Counter(ans))
ans = sorted(list(Counter(ans).values())) 
# 각 숫자를 key, 각 숫자의 개수를 value로 지정하고, 이를 오름차순으로 정렬함.
print(ans)

print(cnt)
print('\n'.join(map(str, ans)))

'''
# dfs

from collections import deque, Counter
from functools import reduce

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt):
    group[x][y] = cnt
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == 1 and group[nx][ny] == 0:
                dfs(nx, ny, cnt)
                
n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]
group = [[0] * n for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            dfs(i, j, cnt)

ans = reduce(lambda x, y : x + y, group)
ans = [x for x in ans if x > 0]
ans = sorted(list(Counter(ans).values()))

print(cnt)
print('\n'.join(map(str, ans)))

'''