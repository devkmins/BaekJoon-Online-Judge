A, B, V = map(int, input().split())

c = 1
tmp = 0

while True:
    if A == V:
        c += 1
        break
    else:
        tmp += A
        if tmp < V:
            tmp -= B
        else:
            break
    c += 1

print(c)
    