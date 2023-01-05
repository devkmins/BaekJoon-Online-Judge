import sys

n = int(input())
prog = [int(input()) for _ in range(n)]
stack = []
m = 0
ans = ''

for p in prog:
    if p > m:
        while p > m:
            m += 1
            stack.append(m)
            ans += '+\n'
        stack.pop()
        ans += '-\n'
    
    else:
        if stack[-1] != p:
            print('NO')
            sys.exit(0)
            
        stack.pop()
        ans += '-\n'
        
print(ans, end='')