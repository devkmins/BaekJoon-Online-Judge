n = int(input())
d = [0] * (n + 1)
d[1] = 1

for i in range(2, n + 1):
    j = 2
    d[i] = d[i - 1] + 1
    while j * j <= i:
        d[i] = min(d[i], d[i - j * j] + 1)
        j += 1

print(d[n])