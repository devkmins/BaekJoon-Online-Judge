import sys

_ = int(sys.stdin.readline())
N = set(map(int, sys.stdin.readline().split()))
_ = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

for m in M:
    if m in N:
        print(1)
    else:
        print(0)

