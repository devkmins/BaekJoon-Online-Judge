B = [int(input()) for _ in range(int(input()))]

stack = []
cnt = 0

for b in B:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)
    
    cnt += len(stack) - 1
    
print(cnt)