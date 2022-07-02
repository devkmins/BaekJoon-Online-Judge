import sys

M, N = int(sys.stdin.readline()), int(sys.stdin.readline())

prime_number = []

for i in range(M, N+1):
    count = 0
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
    if count == 1:
        prime_number.append(i)

if len(prime_number) == 0:
    print(-1)
else:
    print(sum(prime_number))
    print(min(prime_number))