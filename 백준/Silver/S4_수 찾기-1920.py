_ = int(input())
N = list(map(int, input().split()))
_ = int(input())
M = list(map(int, input().split()))

for m in M:
    if m in N:
        print(1)
    else:
        print(0)
