import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    data = a ** b
    if data <= 10:
        print(data)
    else:
        print(str(data)[len(str(data)) - 1])
