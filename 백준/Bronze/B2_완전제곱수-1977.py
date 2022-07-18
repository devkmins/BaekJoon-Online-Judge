'''
해결 방법 -
1. m <= i ** 2 <= n을 구함.
2. i를 1부터 하나씩 증가시키며, i ** 2가 n을 초과할 때 break
'''

M, N = int(input()), int(input())
L = []
i = 1

while i ** 2 <= N:
    if i ** 2 >= M and i ** 2 <= N:
        L.append(i ** 2)
    i += 1
        
if len(L) != 0:
    print(sum(L))
    print(min(L))
else:
    print(-1)