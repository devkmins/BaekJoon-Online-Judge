N = int(input())
c = 0

car_num = list(map(int, input().split()))

for n in car_num:
    if N == n:
        c += 1

print(c)
