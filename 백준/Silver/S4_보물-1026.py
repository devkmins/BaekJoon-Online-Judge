'''
해결 방법 -
1. A를 오름차순으로, B를 내림차순으로 정렬하여 곱할 시 최솟값이 나옴.
2. B는 재배열하면 안 되므로, A의 최소값과 B의 최대값을 곱한 후 pop 해 준다.
'''
import sys

result = 0

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

for _ in range(N):
    result = result + min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
    
print(result)