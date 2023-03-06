import sys

n = int(input())

max_d, min_d = [0] * 3, [0] * 3
max_temp, min_temp = [0] * 3, [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_temp[j] = a + max(max_d[j], max_d[j + 1])
            min_temp[j] = a + min(min_d[j], min_d[j + 1])
        elif j == 1:
            max_temp[j] = b + max(max_d[j - 1], max_d[j], max_d[j + 1])
            min_temp[j] = b + min(min_d[j - 1], min_d[j], min_d[j + 1])
        else:
            max_temp[j] = c + max(max_d[j], max_d[j - 1])
            min_temp[j] = c + min(min_d[j], min_d[j - 1])
            
    for j in range(3):
        max_d[j] = max_temp[j]
        min_d[j] = min_temp[j]
        
print(max(max_d), min(min_d))