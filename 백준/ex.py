'''
리스트 내포 사용할 것
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)

print(result)

->

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]

lambda도 사용할 것 -> def와 동일한 역할을 한다.
add = lambda a, b: a+b
result = add(3, 4)n o
'''

'''
n = 5
print(n * (n + 1) // 2)
'''

'''
a = ['abc', 'def']

print(dir(a))

print(a.__add__(['ghi']))
print(a.__getitem__(0))
'''

'''
import time

start = time.time()

a = [range(1000)]

for i in range(len(a)):
    b = a[i]
    # for i in a: b = a --> 4
    
end = time.time()

print(end - start)
'''

#print(f'Objects weighing {n:.2f} on Earth will weigh {n * 0.167:.2f} on the moon.')
