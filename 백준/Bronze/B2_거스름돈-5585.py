n = int(input())
n = 1000 - n

count = 0

change = [500, 100, 50, 10, 5, 1]

for money in change:
    count += n // money
    n %= money

print(count)
