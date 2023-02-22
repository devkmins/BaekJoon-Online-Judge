h, y = map(int, input().split())

d = [0] * (y + 1)
d[0] = h

for i in range(y + 1):
    if i - 5 >= 0:
        d[i] = max(d[i - 5] * 1.35, d[i - 3] * 1.2, d[i - 1] * 1.05)
    elif i - 3 >= 0:
        d[i] = max(d[i - 3] * 1.2, d[i - 1] * 1.05)
    elif i - 1 >= 0:
        d[i] = d[i - 1] * 1.05
        
    d[i] = int(d[i])
    
print(d[y])