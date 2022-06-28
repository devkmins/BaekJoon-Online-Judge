N = int(input())
apple = 0

for n in range(N):
    a, b = list(map(int, input().split()))
    apple += b % a

print(apple)
