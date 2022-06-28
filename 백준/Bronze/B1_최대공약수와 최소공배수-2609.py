numbers = list(map(int, input().split()))
n_list_first, n_list_second = [], []

for n in numbers:
    if n == numbers[0]:
        for num in range(2, n+1):
            while True:
                if n % num == 0:
                    n //= num
                    n_list_first.append(num)
                else:
                    break
    else:
        for num in range(2, n+1):
            while True:
                if n % num == 0:
                    n //= num
                    n_list_second.append(num)
                else:
                    break

intersection = list(set(n_list_first) & set(n_list_second))
greatest = 1

for i in intersection:
    greatest *= i

lowest_first = numbers[0]
lowest_second = numbers[1]
lowest_list = []

for i in intersection:
    while True:
        if lowest_first % i == 0 and lowest_second % i == 0:
            lowest_first //= i
            lowest_second //= i
            lowest_list.append(i)
        else:
            break

    lowest_list.append(lowest_first)
    lowest_list.append(lowest_second)

lowest = 1

for i in lowest_list:
    lowest *= i

print(greatest)
print(lowest)
