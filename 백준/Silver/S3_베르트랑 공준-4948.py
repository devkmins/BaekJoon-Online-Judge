MAX = 246913

check = [0] * (MAX + 1)
check[0] = check[1] = True

for i in range(2, MAX + 1):
    if not check[i]:
        j = i + i
        while j <= MAX:
            check[j] = True
            j += i

while True:
    n = int(input())
    if n == 0:
        break
    
    print(check[n + 1:2 * n + 1].count(0))