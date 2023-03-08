n = int(input())
d = [0] * (n + 1)

try:
    d[2] = 1
except:
    pass

for i in range(3, n + 1):
    d[i] = (i - 1) * (d[i - 1] + d[i - 2]) % 1000000000
    
print(d[n])