def go(index, start, n, m):
    if index == m:
        d.append(tuple(answer))
        return
    
    for i in range(start, n):
        if check[i]:
            continue
        
        check[i] = True 
        answer[index] = nums_list[i]
        go(index + 1, i, n, m)
        check[i] = False

n, m = map(int, input().split())
nums_list = list(map(int, input().split()))
nums_list.sort()
answer = [0] * m
check = [False] * n
d = []

go(0, 0, n, m)
d = list(set(d))
d.sort()

for i in d:
    print(" ".join(map(str, i)))