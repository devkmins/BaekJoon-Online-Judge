n = int(input())
d = [0] * (n + 1)

if n >= 2:
    d[2] = 2
    for i in range(3, n + 1):
        d[i] = d[i - 1] * 3

print(d[n])