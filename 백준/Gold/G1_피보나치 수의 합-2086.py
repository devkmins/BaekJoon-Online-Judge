def fib_iter(a, b):
    last = 0
    current = 1
    fib_sum = 0
    for i in range(1, b+1):
        tmp = current
        if i >= a:
            fib_sum += current
            #print(f'sum: {fib_sum}')
        #print(f'current: {current}')
        current += last
        last = tmp
    return fib_sum


a, b = list(map(int, input().split()))

print(fib_iter(a, b))
