import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

count_a, count_b = 0, 0

for a, b in zip(A, B):
    if a > b:
        count_a += 1
    elif b > a:
        count_b += 1

if count_a > count_b:
    print('A')
elif count_b > count_a:
    print('B')
else:
    print('D')