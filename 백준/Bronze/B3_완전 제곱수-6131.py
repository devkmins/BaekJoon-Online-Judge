n = int(input())
cnt = 0

for b in range(1, 500):
    for a in range(b + 1, 501):
        if a ** 2 == b ** 2 + n:
            cnt += 1
            
print(cnt)