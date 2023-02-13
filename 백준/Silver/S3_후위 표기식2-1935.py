N = int(input())
postfix = input()
operand = [int(input()) for _ in range(N)]
stack = []

A = ord('A')
Z = ord('Z')

for ch in postfix:
    if A <= ord(ch) <= Z:
        stack.append(operand[ord(ch) - A])
    else:
        op2 = stack.pop()
        op1 = stack.pop()
        if ch == '+':
            stack.append(op1 + op2)
        elif ch == '-':
            stack.append(op1 - op2)
        elif ch == '*':
            stack.append(op1 * op2)
        elif ch == '/':
            stack.append(op1 / op2)

print('%.2f' % stack[-1])