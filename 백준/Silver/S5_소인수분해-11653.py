N = int(input())

for num in range(2, N+1):
    while True:
        if N % num == 0:
            N //= num
            print(num)
        else:
            break
