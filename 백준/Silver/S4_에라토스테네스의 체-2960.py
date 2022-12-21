n, k = map(int, input().split())

check = [0] * (n + 1)
check[0] = check[1] = True
prime = []

for i in range(2, n + 1):
    if not check[i]:
        prime.append(i)
        j = i + i
        while j <= n:
            check[j] = True
            if j in prime:
                pass
            else:
                prime.append(j)
            j += i
            
print(prime[k - 1])