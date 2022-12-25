import time

start = time.time()

n = int(input())

if n % 2 == 0:
    print('CY')
else:
    print('SK')
    
end = time.time()

print(end - start)