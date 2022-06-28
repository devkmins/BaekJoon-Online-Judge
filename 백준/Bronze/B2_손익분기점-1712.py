A, B, C = list(map(int, input().split()))

notebook = C - B

if notebook < 0:
    print(-1)
else:
    print(A // notebook + 1)
