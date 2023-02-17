a, b = input(), input()
ans = ''
temp = ''
d = []

for i, j in zip(a, b):
    ans += i
    ans += j

while len(ans) != 2:
    for i in range(1, len(ans)):
        plus = int(ans[i]) + int(ans[i - 1])
        if plus >= 10:
            temp += str(plus)[1]
        else:
            temp += str(plus)
    
    d.append(temp)
    ans = temp
    temp = ''
        
print(d[-1])
        