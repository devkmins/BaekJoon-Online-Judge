def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())

for _ in range(n):
    m = list(map(int, input().split()))
    gcd_values = []
    
    for i in range(len(m) - 1):
        for j in range(i + 1, len(m)):
            n1, n2 = m[i], m[j]
            gcd_values.append(gcd(n1, n2))
    
    print(max(gcd_values))