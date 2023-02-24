n = int(input())
a = list(map(int, input().split()))

d = [0] * n
min_val = a[0]

for i in range(1, n):
    d[i] = max(d[i - 1], a[i] - min_val)
    min_val = min(min_val, a[i])
    
print(" ".join(map(str, d)))