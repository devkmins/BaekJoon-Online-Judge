t = int(input())

for _ in range(t):
    n = int(input())
    time = 0
    cnt = 0
    
    while True:
        if cnt + cnt ** 2 <= n:
            time = cnt
            cnt += 1
        else:
            print(time)
            break