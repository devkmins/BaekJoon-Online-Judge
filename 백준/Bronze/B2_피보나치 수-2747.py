def fib_iter(n):
    if n < 2:
        return n

    last = 0
    current = 1
    for _ in range(2, n+1):  # 입력받은 수 - 1만큼 반복
        tmp = current  # temporary: 일시적인
        current += last
        last = tmp
    return current


print(fib_iter(int(input())))
