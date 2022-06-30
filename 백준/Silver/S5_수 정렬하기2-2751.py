'''
해결 방법 -
1. 입력 받은 수들을 리스트에 저장
2. 정렬
3. for문으로 출력
'''

import sys

num_list = []

N = int(input())

for _ in range(N):
    num_list.append(int(sys.stdin.readline()))
    
num_list.sort()

for i in num_list:
    print(i)
