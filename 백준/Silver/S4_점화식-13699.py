N = int(input())
d = [0] * (N + 1)
d[0] = 1

for i in range(1, N + 1):
    for a, b in zip([j for j in range(i)], [j for j in range(i - 1, -1, -1)]):
        d[i] += d[a] * d[b]
        
print(d[N])