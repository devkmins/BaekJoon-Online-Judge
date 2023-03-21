import sys

N, M = map(int, input().split())

a = [0] * M

def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(1, n + 1):
        a[index] = i
        go(index + 1, n, m)
        
go(0, N, M)