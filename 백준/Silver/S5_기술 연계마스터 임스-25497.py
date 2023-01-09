n = int(input())
skills = list(input())

l_r_stack = []
s_k_stack = []
cnt = 0

for i in skills:
    if ord(i) >= ord('1') and ord(i) <= ord('9'):
        cnt += 1
    elif i == 'L':
        l_r_stack.append(i)
    elif i == 'S':
        s_k_stack.append(i)
    elif l_r_stack and i == 'R':
        if l_r_stack[-1] == 'L':
            l_r_stack.pop()
            cnt += 1
        else:
            break
    elif s_k_stack and i == 'K':
        if s_k_stack[-1] == 'S':
            s_k_stack.pop()
            cnt += 1
        else:
            break
    else:
        break
            
print(cnt)
