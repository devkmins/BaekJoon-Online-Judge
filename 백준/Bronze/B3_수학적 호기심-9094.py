import sys

def check(n, m):
    cnt = 0
    
    for i in range(1, n):
        for j in range(i + 1, n):
            val = (i ** 2 + j ** 2 + m) / (i * j)
            if val == int(val):
                cnt += 1
                
    return cnt

t = int(input())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(check(n, m))