n = int(input())

string = input()

stack = []
check = [0] * n

for i in range(n):
    if string[i] == '(':
        stack.append(i)
    else:
        if stack:
            check[i] = check[stack[-1]] = 1
            stack.pop()
            
ans, cnt = 0, 0

print(check)

for num in check:
    if num == 1:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
        
print(ans)