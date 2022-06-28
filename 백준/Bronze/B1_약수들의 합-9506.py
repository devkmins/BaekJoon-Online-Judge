while True:
    n = int(input())
    if n == -1:
        break
    else:
        numbers = []
        for num in range(1, n+1):
            while True:
                if n % num == 0:
                    n //= num
                    numbers.append(num)
                else:
                    break
        if n == sum(numbers):
            print(numbers)
            #print(f'{n} = ')
