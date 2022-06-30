time = 0

for i in range(4):
    N = int(input())
    time += N
    
print(time // 60)
print(time % 60)