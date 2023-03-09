def prime(k):
    check = [False] * (k + 1)
    prime = []
    
    for i in range(2, k + 1):
        if not check[i]:
            prime.append(i)
            j = i + i
            while j <= k:
                check[j] = True
                j += i
                
    return prime

def answer(k):
    prime_list = prime(k)
    for i in range(2, k):
        if p % i == 0:
            if i in prime_list:
                return f"BAD {i}"
    
    return "GOOD"
                
p, k = map(int, input().split())

print(answer(k))