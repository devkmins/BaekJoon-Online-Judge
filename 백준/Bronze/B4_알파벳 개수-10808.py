import string

I = list(input())
S = string.ascii_lowercase

for i in S:
    print(I.count(i), end=' ')
print()