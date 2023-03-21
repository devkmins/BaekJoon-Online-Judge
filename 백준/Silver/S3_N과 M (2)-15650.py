# O(2 ** n) 코드

import sys

N, M = map(int, input().split())

a = [0] * M

def go(index, selected, n, m):
    if selected == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    if index > n:
        return
    a[selected] = index
    go(index + 1, selected + 1, n, m)
    a[selected] = 0
    go(index + 1, selected, n, m)
    
go(1, 0, N, M)

'''
# O(N!) 코드

import sys

N, M = map(int, input().split())

c = [False] * (N + 1)
a = [0] * M

def go(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(start, n + 1):
        a[index] = i
        go(index + 1, i + 1, n, m)
        
go(0, 1, N, M)
'''