mbti = input()

for i in mbti:
    if i == 'I':
        print('E', end='')
    elif i == 'E':
        print('I', end='')
    elif i == 'N':
        print('S', end='')
    elif i == 'S':
        print('N', end='')
    elif i == 'T':
        print('F', end='')
    elif i == 'F':
        print('T', end='')
    elif i == 'J':
        print('P', end='')
    elif i == 'P':
        print('J', end='')
print()