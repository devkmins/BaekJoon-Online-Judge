N = int(input())
numbers = list(map(int, input().split()))

ans = [0] * N
stack = [0]

for i in range(1, N):
    if not stack:
        stack.append(i)
        print(f'if not stack === {stack}')
    while stack and numbers[stack[-1]] < numbers[i]:
        print(f'for while stack === {stack}')
        print(f'for while numbers[stack[-1]] === {numbers[stack[-1]]}')
        print(f'for while numbers[i] === {numbers[i]}')
        print(f'for while ans === {ans}')
        ans[stack.pop()] = numbers[i]
    stack.append(i)
    print(f'for stack === {stack}')
    
while stack:
    print(f'while stack === {stack}')
    print(f'while ans === {ans}')
    ans[stack.pop()] = -1

print(' '.join(map(str, ans)))