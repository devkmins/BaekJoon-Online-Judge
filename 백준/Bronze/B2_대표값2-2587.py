num_list = []

for _ in range(5):
    num_list.append(int(input()))

print(int(sum(num_list) / len(num_list)))

num_list.sort()
print(num_list[2])

'''
n = len(num_list)

if n % 2 == 1:
    for i in range(0, int((n-1)/2)):
        num_list.remove(num_list[i])
    # 이 코드가 먼저 실행되므로, 뒤의 값은 실행이 안 된다.

    for i in range(n-1, int((n+1)/2)):
        num_list.remove(num_list[i])

    print(num_list)

else:
    for i in range(0, int((n-2)/2)):
        num_list.remove(num_list[i])

    for i in range(n-1, int((n+2)/2)):
        num_list.remove(num_list[i])

    print(num_list)
'''
