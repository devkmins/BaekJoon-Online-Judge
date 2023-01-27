n = int(input())

s = n - 1
c = 1

for i in range(1, n + 1):
    print(s * ' ', end='')
    print(i * '* ')
    s -= 1
    
'''
다른 사람 코드

n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * (i - 1) + "*")
'''