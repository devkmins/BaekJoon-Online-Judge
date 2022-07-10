digits = list('9780921418')
s = 0

for _ in range(3):
    digits.append(input())
    
for i in range(len(digits)):
    if i % 2 == 0:
        s += int(digits[i]) * 1
    else:
        s += int(digits[i]) * 3
        
print(f'The 1-3-sum is {s}')