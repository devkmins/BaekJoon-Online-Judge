S = list(input())

stack = []
tmp = 1
answer = 0

for i in range(len(S)):
    if S[i] == '(':
        stack.append(S[i])
        tmp *= 2
    elif S[i] == '[':
        stack.append(S[i])
        tmp *= 3
    elif S[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if S[i - 1] == '(':
            answer += tmp
        tmp //= 2
        stack.pop()
    elif S[i] == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if S[i - 1] == '[':
            answer += tmp
        tmp //= 3
        stack.pop()
        
if stack:
    answer = 0

print(answer)