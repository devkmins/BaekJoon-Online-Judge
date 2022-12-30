d = [0] * 11
d[0] = 1

for i in range(1, 11):
    if i - 1 >= 0:
        d[i] += d[i - 1]
    if i - 2 >= 0:
        d[i] += d[i - 2]
    if i - 3 >= 0:
        d[i] += d[i - 3]
        
print(d)
        
t = int(input())

for _ in range(t):
    n = int(input())
    print(d[n])
    
    
'''
# 브루트 포스

def go(sum_n, goal):
    if sum_n > goal:
        return 0
    if sum_n == goal:
        return 1
    
    now = 0
    
    for i in range(1, 4):
        now += go(sum_n + i, goal)
        
    return now

for _ in range(int(input())):
    n = int(input())
    print(go(0, n))
'''