n = int(input())
cnt = 0

for i in range(1, n + 1):
    s = sum(map(int, str(i)))
    if i % s == 0:
        cnt += 1
        
print(cnt)