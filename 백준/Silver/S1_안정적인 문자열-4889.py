result = []

while True:
    data = input()
    cnt = 0
    stack = []
    
    if '-' in data:
        break
    for i in data:
        if i == '}':
            if stack:
                stack.pop()
            else:
                cnt += 1
                stack.append('{')
        else:
            stack.append(i)

    cnt += len(stack) // 2
    result.append(cnt)
    
for i in range(len(result)):
    print(f'{i + 1}. {result[i]}')