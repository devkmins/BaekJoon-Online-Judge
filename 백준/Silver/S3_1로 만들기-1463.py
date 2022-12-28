N = int(input())
d = [0] * (N + 1)

for i in range(2, N + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1
    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1
       
print(d[N])

'''
# Top-down 방식으로, 재귀를 사용하기 때문에 시간 초과가 남. 파이썬은 Bottom-up 방식이 더 나음.

import sys
sys.setrecursionlimit(10000000)

def go(n):
    if n == 1:
        return 0
    if d[n] > 0:
        return d[n]
    d[n] = go(n - 1) + 1
    if n % 2 == 0:
        temp = go(n // 2) + 1
        if d[n] > temp:
            d[n] = temp
    if n % 3 == 0:
        temp = go(n // 3) + 1
        if d[n] > temp:
            d[n] = temp
    return d[n]

N = int(input())
d = [0] * (N + 1)

print(go(N))
'''