n = int(input())

s = n - 1
c = 1

for i in range(1, 2 * n, 2):
    print(s * ' ', end='')
    print(i * '*')
    s -= 1
    
for i in range(2 * (n - 1) - 1, 0, -2):
    print(c * ' ', end='')
    print(i * '*')
    c += 1