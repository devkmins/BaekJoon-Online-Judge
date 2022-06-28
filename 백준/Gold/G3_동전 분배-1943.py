T = int(input())


def calc(number):
    for n in number:
        for num in range(2, n+1):
            while True:
                if n % num == 0:
                    n //= num
                    numbers.append(num)
                else:
                    break


for _ in range(T):
    numbers = []
    small = 1
    case = list(map(int, input().split()))
    if case.count(1) >= 1:
        for n in case:
            small *= n
        print(small)
    else:
        calc(case)
        for n in list(set(numbers)):
            small *= n
        print(small)