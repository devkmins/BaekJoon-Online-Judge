import sys

N = int(input())

L = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    L.append([b, a])

L.sort()

for i in L:
    print(i[1], i[0])