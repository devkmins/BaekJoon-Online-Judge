T = int(input())

d = [0] * 10001
d[0], d[1] = 0, 1

for i in range(2, 10001):
    d[i] = d[i - 1] + d[i - 2]

for i in range(1, T + 1):
    P, Q = map(int, input().split())
    print(f'Case #{i}: {d[P] % Q}')