n = int(input())
a = [int(input()) for _ in range(n)]
d = [0] * n

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            
print(n - max(d))