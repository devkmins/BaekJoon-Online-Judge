'''
해결 방법 -
1. 입력 받은 값들을 리스트 형태로 만들어 리스트에 추가
2. 최소값을 pop -> 시간 초과
3. 정렬 후 정렬된 값 출력
'''

import sys

N = int(input())
L = []

for _ in range(N):
    [a, b] = map(int, sys.stdin.readline().split())
    L.append([a, b])
    
sort_L = sorted(L)

for i in range(N):
    print(sort_L[i][0], sort_L[i][1])

# 내 코드
'''
import sys

N = int(input())
L = []

for _ in range(N):
    [coord] = map(int, sys.stdin.readline().split())
    L.append(coord)
    
for _ in range(N):
    print(*L.pop(L.index(min(L))))
'''