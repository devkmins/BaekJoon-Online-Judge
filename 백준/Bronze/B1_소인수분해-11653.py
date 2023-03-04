'''
해결 방법 -
1. 변수를 2로 지정하고, 입력 받은 n을 나눠줌. 
2. 이때 나머지가 0이면, 계속 나누어 줌.
3. 아닐 경우 변수 + 1
4. 입력 받은 수를 변수로 나눈 몫이 0인 경우 종료
'''

# 백준 코드

n = int(input())
i = 2
while i*i <= n:
    while n % i == 0:
        print(i)
        n //= i
    i += 1

if n > 1:
    print(n)

'''
예전 코드 -

N = int(input())

for num in range(2, N+1):
    while True:
        if N % num == 0:
            N //= num
            print(num)
        else:
            break
'''