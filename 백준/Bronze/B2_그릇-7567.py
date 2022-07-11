'''
해결 방법 -
1. 맨 밑의 그릇의 길이를 10이라 할 때, index + 1의 그릇의 방향과 현재 그릇의 방향이 같으면 +5, 다르면 +10
'''

bracket = input()

c = 10

for i in range(len(bracket) - 1):
    if bracket[i+1] == bracket[i]:
        c += 5
    else:
        c += 10
        
print(c)