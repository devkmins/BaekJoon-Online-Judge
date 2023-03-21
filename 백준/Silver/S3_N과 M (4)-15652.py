import sys

N, M = map(int, input().split())

c = [False] * (N + 1)
a = [0] * N

def go(index, start, n, m):
    if index == m:
        for i in range(m):
            sys.stdout.write(str(a[i]) + ' ')
        sys.stdout.write('\n')
        return
    for i in range(start, n + 1):
        c[i] = True
        a[index] = i
        go(index + 1, i, n, m)
        c[i] = False
        
go(0, 1, N, M)

'''
# 선택 코드

import sys

n, m = map(int, input().split())
cnt = [0] * (n + 1)

def go(index, selected, n, m):
    if selected == m:
        for i in range(1, n + 1):
            for j in range(cnt[i]):
                sys.stdout.write(str(i) + ' ')
        sys.stdout.write('\n')
        return
    if index > n:
        return
    for i in range(m - selected, 0, -1):
        cnt[index] = i
        go(index + 1, selected + i, n, m)
    cnt[index] = 0
    go(index + 1, selected, n, m)

go(1, 0, n, m)

'''