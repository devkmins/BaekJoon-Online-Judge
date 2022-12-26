# 백준 코드
def valid(s):
    cnt = 0
    
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return "NO"
    
    if cnt == 0:
        return "YES"
    else:
        return "NO"

T = int(input())

for _ in range(T):
    print(valid(input()))

'''
내가 쓴 코드 -
())(()와 같이 ( 후에 )) 일 때, )) 앞에는 열린 괄호가 하나 밖에 없으므로, 이것 또한 처리해 줘야 함.
그렇기 때문에 밑의 코드는 틀렸음.

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    cnt = 0
    brackets = input().rstrip()
    for i in brackets:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
    if cnt == 0:
        print("YES")
    else:
        print("NO")
'''