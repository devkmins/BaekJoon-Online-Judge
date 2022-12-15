s, boom = input(), input()

stack = []
last_boom = boom[-1]

for i in s:
    stack.append(i)
    if stack[-1] == last_boom and "".join(stack[-len(boom):]) == boom:
        for _ in range(len(boom)):
            stack.pop()
        
if stack:
    print("".join(stack))
else:
    print('FRULA')