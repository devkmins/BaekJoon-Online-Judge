from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2] # 8가지 방향
dy = [1, 2, 2, 1, -1, -2, -2, -1] # 8가지 방향
t = int(input()) # 테스트 케이스

for _ in range(t):
    n = int(input()) # 체스판의 한 변의 길이
    sx, sy = map(int, input().split()) # 나이트가 현재 있는 칸
    ex, ey = map(int, input().split()) # 나이트가 이동하려는 칸
    d = [[-1] * n for _ in range(n)] # 체크해 주는 개수
    q = deque()
    q.append((sx, sy)) # 나이트가 현재 있는 칸을 저장
    d[sx][sy] = 0 # 나이트가 현재 있는 칸을 0
    
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k] # 8가지 방향
            if 0 <= nx < n and 0 <= ny < n: # 체스판 크기 내에서
                if d[nx][ny] == -1: # 방문하지 않은 경우
                    d[nx][ny] = d[x][y] + 1 # 현재 위치의 값에 +1
                    q.append((nx, ny)) # 큐에 추가
                         
    print(d[ex][ey]) # 인덱스에 해당하는 위치의 값을 출력