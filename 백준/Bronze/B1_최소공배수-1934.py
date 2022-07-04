'''
해결 방법 -
1. 두 수의 최대 공약수를 구한다. (나누고 난 후의 나머지)
2. 입력 받은 두 수를 곱한 뒤에, 최대 공약수를 나누어준다.
'''

import sys

T = int(input())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    A, B = a, b
    while a % b != 0:
        a, b = b, a % b
    print(A * B // b)

# 이전에 내가 작성한 코드
'''
T = int(input())

for _ in range(T):
    L = []
    min_L = []
    A, B = map(int, input().split())
    if min(A, B) == 1:
        print(max(A, B))
    else:
        for i in range(1, max(A, B)+1):
            L.append(min(A, B) * i)
        for i in range(1, min(A, B)+1):
            L.append(max(A, B) * i)
        for i in L:
            if L.count(i) == 2:
                min_L.append(i)
            else:
                continue
        print(min(set(min_L)))
'''