N = int(input())
numbers = list(map(int, input().split()))

freq = [0] * 1000001

for i in range(N):
    freq[numbers[i]] += 1
    
ans = [0] * N
stack = [0]

for i in range(1, N):
    if not stack:
        stack.append(i)
        print(f'if stack === {stack}')
    while stack and freq[numbers[stack[-1]]] < freq[numbers[i]]:
        print(f'while freq[numbers[stack[-1]]] === {freq[numbers[stack[-1]]]}')
        print(f'while freq[numbers[i]] === {freq[numbers[i]]}')
        ans[stack.pop()] = numbers[i]
        print(f'while ans === {ans}')
    stack.append(i)
    print(f'stack === {stack}')
    
while stack:
    ans[stack.pop()] = -1
    
print(' '.join(map(str, ans)))