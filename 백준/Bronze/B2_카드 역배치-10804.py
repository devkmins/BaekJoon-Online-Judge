card = list(range(1, 21))

for _ in range(10):
    a, b = list(map(int, input().split()))
    card[a-1:b] = list(reversed(card[a-1:b]))

for i in card:
    print(i, end=' ')

print()
