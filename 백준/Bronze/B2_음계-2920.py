I = list(map(int, input().split()))

asc = list(range(1, 9))
des = list(range(8, 0, -1))

if I == asc:
    print('ascending')
elif I == des:
    print('descending')
else:
    print('mixed')