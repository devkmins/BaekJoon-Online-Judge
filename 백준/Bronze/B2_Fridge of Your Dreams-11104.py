'''
해결 방법 -
1. 2진수를 10진수로 변환
'''

T = int(input())

for _ in range(T):
    binary = input()
    print(int(binary, 2))