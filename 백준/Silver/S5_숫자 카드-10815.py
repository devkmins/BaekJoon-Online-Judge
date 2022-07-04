_ = int(input())
N = set(map(int, input().split()))
_ = int(input())
M = list(map(int, input().split()))

for i in M:
    if i in N:
        print(1, end=' ')
    else:
        print(0, end=' ')
        
print()