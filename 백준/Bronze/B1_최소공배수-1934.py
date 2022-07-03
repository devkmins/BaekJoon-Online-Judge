T = int(input())

for _ in range(T):
    L = []
    min_L = []
    A, B = map(int, input().split())
    if min(A, B) == 1:
        print(max(A, B))
    else:
        for i in range(1, max(A, B)+1):
            L.append(min(A, B) * i)
        for i in range(1, min(A, B)+1):
            L.append(max(A, B) * i)
        for i in L:
            if L.count(i) == 2:
                min_L.append(i)
            else:
                continue
        print(min(set(min_L)))