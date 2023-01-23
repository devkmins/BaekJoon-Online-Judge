N = int(input())
d = [[[0], []] for _ in range(N + 1)]
d[1][0] = 0
d[1][1] = [1]

for i in range(2, N + 1):
    d[i][0] = d[i - 1][0] + 1
    d[i][1] = d[i - 1][1] + [i]
    if i % 2 == 0 and d[i][0] > d[i // 2][0] + 1:
        d[i][0] = d[i // 2][0] + 1
        d[i][1] = d[i // 2][1] + [i]
    if i % 3 == 0 and d[i][0] > d[i // 3][0] + 1:
        d[i][0] = d[i // 3][0] + 1
        d[i][1] = d[i // 3][1] + [i]
        
print(d[N][0])
print(*reversed(d[N][1]))