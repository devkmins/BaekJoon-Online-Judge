N = int(input())
d = [0] * 1000001
d[1] = 1

for i in range(2, N + 1):
    d[i] = d[i - 1] + d[i - 2]
    d[i] %= 1000000007
    
print(d[N])