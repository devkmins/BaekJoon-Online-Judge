'''
해결 방법 -
1. 입력 받은 수가 0이 아닌 경우에 리스트에 저장
2. 0일 경우 pop
'''

K = int(input())

note = []

for _ in range(K):
    N = int(input())
    if N != 0:
        note.append(N)
    else:
        note.pop()
    
print(sum(note))