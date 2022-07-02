# 덱을 이용한 구현
from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])

# -------------------------------------------

# 규칙을 찾아 구현
input = int(input())
square = 2

while True:
    if (input == 1 or input == 2):
        print(input)
        break
    square *= 2
    if (square >= input):
        print((input - (square // 2)) * 2)
        break
    
# https://tooo1.tistory.com/88

# 내가 쓴 코드
'''
N = int(input())

card = list(range(1, N+1))

turn = 1

while True:
    if len(card) == 1:
        print(*card)
        break
    if turn == 1:
        card.remove(card[0])
        tmp = 0
        tmp = card[0]
        card.remove(card[0])
        card.append(tmp)
'''