N = int(input())
P = list(map(int, input().split()))
P.sort()

value = 0

for l in range(1, len(P)+1):
    count = 0
    for p in P:
        count += 1
        value += p
        if l == count:
            break

print(value)
