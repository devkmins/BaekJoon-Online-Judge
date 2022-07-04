import sys

N = int(input())

L = []

for _ in range(N):
    L.append(int(sys.stdin.readline()))
    
L.sort()

for i in L:
    print(i)