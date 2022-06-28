L, P = list(map(int, input().split()))
people = list(map(int, input().split()))

for p in people:
    print(p - L * P, end=' ')

print()
