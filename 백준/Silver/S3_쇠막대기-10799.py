bracket = input()

stack = []

sticks = 0

for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append(i)
    else:
        if stack[-1] + 1 == i:
            stack.pop()
            sticks += len(stack)
        else:
            stack.pop()
            sticks += 1
            
print(sticks)