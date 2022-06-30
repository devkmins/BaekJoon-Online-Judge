'''
해결 방법 -
2143과 같이 입력을 받으므로, str로 입력을 받은 후, list로 타입 캐스팅 해주어 2, 1, 4, 3으로 만들어 주고,
map을 사용하여 정수로 만들어 준 뒤, 다시 list로 만들어 준다.
'''

a = list(map(int, list(input())))
a.sort(reverse=True)

for i in a:
    print(i, end='')
    
print()

