import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
d = [0]
temp = 0

for i in arr:
	temp += i
	d.append(temp)

for _ in range(m):
	i, j = map(int, sys.stdin.readline().split())
	print(d[j] - d[i - 1])