import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = list(map(int, input().split()))
    n = n[1:]
    result = 0
    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            result += gcd(n[i], n[j])
    print(result)
    
'''
백준 코드 - 

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    n = a[0]
    a = a[1:]
    ans = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            ans += gcd(a[i], a[j])
    print(ans)
'''