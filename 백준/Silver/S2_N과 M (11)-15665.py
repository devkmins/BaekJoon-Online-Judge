def go(index, n, m):
    if index == m:
        d.append(tuple(answer))
        return
    
    for i in range(n):
        answer[index] = nums_list[i]
        go(index + 1, n, m)

n, m = map(int, input().split())
nums_list = list(map(int, input().split()))
nums_list.sort()
answer = [0] * m
d = []

go(0, n, m)
d = list(set(d))
d.sort()

for i in d:
    print(" ".join(map(str, i)))