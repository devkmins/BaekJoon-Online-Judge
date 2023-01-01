n = int(input())

MAX = 1003002
check = [False] * (MAX + 1)
check[0] = check[1] = True
prime = []

for i in range(2, MAX):
    if check[i] == False:
        prime.append(i)
        j = i + i
        while j <= MAX:
            check[j] = True
            j += i
            
for p in prime:
    if str(p) == str(p)[::-1] and p >= n:
        print(p)
        break