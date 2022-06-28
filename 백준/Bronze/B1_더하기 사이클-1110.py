n = input()
if int(n) < 10:
    n += '0'
num = n
cnt = 0

while True:
    a, b = n[0], n[1]
    while True:
        c = str(sum(list(map(int, (a, b)))))
        if int(c) > 9:
            c = c[1]
        n = b + c
        break
    cnt += 1
    if num == n:
        break

print(cnt)
