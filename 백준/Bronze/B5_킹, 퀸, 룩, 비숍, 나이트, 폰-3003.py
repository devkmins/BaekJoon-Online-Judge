piece = [1, 1, 2, 2, 2, 8]

I = list(map(int, input().split()))

for i, j in zip(I, piece):
    print(j - i, end=' ')
print()