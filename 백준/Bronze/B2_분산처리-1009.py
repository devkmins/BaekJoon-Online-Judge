for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    data = a ** b
    if data <= 10:
        print(data)
    else:
        print(str(data)[len(str(data)) - 1])
