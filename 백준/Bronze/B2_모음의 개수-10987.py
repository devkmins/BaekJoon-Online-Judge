v = 'aeiou'
count = 0

W = list(input())

for i in W:
    if i in v:
        count += 1
        
print(count)