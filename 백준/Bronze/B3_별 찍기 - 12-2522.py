n = int(input())

c = n - 1
m = 0

for i in range(1, 2 * n):
    if i > n:
        m += 2
        c += 1
        print(' ' * c, end='')
        print('*' * (i - m))
    else:
        if c == 0:
            print(' ' * c, end='')
            print('*' * i)
            c = 0
        else:
            print(' ' * c, end='')
            print('*' * i)
            c -= 1