'''
해결 방법 -
1. 1부터 차례대로 더해준다.
2. 더한 값이 입력 받은 값을 넘어서면, break
3. count를 출력
'''

S = int(input())

sum_num = 0
c = 0

while True:
    c += 1
    sum_num += c
    if sum_num > S:
        break
    
print(c-1)