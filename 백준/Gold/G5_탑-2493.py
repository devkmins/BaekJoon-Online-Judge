n = int(input())
top = list(map(int, input().split()))

ans = [0] * n
stack = []

for i in range(n - 1, -1, -1):
    print(i)
    if not stack:
        stack.append(i)
    while stack and top[stack[-1]] < top[i]:
        ans[stack.pop()] = i + 1
    stack.append(i)
    
print(' '.join(map(str, ans)))