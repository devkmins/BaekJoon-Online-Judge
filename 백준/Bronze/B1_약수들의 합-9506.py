while True:
    n = int(input())
    if n == -1:
        break
    else:
        numbers = []
        p = ''
        for num in range(1, n):
            if n % num == 0:
                numbers.append(num)
            else:
                pass
        if n == sum(numbers):
            for i in numbers:
                if numbers.index(i) == 0:
                    p += f'{i}'
                else:
                    p += f' + {i}'
            print(f'{n} = {p}')
        else:
            print(f'{n} is NOT perfect.')
