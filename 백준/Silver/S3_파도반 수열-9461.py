d = [0] * 101
d[0] = d[1] = d[2] = 1

for i in range(3, 101):
    d[i] = d[i - 2] + d[i - 3]

T = int(input())

for _ in range(T):
    n = int(input())
    print(d[n - 1])