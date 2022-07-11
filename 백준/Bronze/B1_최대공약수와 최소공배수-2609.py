'''
해결 방법 -
유클리드 호제법을 사용
a, b(a > b)가 있을 때, a / b의 나머지를 r이라 하면, a와 b의 최대공약수는 b와 r의 최대 약수
b / r의 나머지가 r'이면, r / r' ...반복
반복하여 나머지가 0일 될 때, 나누는 수가 최대 공약수

최소 공배수는 a * b를 a와 b의 최대공약수로 나누어 준 것.
(a, b는 서로수)
'''

a, b = map(int, input().split())
A, B = a, b

while B > 0:
     A, B = B, A % B

print(A)
print(a * b // A)

'''
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b / gcd(a, b)
'''