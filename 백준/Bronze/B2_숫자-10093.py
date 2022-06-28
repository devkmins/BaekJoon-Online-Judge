a, b = map(int, input().split())

a = min(a, b)
b = max(a, b)

numbers = [i for i in range(a+1, b)]

print(len(numbers))

for i in numbers:
    print(i, end=' ')

if (a + 1) != b and a != b:
    print()
