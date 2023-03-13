from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
check = [[False] * n for _ in range(n)]
comb = list(combinations(range(n), 3))
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    check[a - 1][b - 1] = True
    check[b - 1][a - 1] = True

for i in comb:
    if check[i[0]][i[1]] or check[i[0]][i[2]] or check[i[1]][i[2]]:
        continue
    cnt += 1
   
print(cnt)