N, K = list(map(int, input().split()))

coins = []

count = 0

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

for c in coins:
    count += K // c
    K %= c

print(count)
