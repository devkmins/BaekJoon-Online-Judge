MAX = 7368788
check = [False] * (MAX + 1)
check[0] = check[1] = True
prime = []

for i in range(2, MAX + 1):
    if not check[i]:
        check[i] = i
        prime.append(i)
        j = i + i
        while j <= MAX:
            check[j] = True
            j += i
            
K = int(input())

print(prime[K - 1])