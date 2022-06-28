c = 0
process_list = []


def hanoi_tower(n, fr, tmp, to):
    global c
    if n == 1:
        process_list.append(f'{fr} {to}')
        #print(fr, to)
        c += 1
    else:
        hanoi_tower(n-1, fr, to, tmp)
        process_list.append(f'{fr} {to}')
        #print(fr, to)
        hanoi_tower(n-1, tmp, fr, to)
        c += 1


hanoi_tower(int(input()), 1, 2, 3)
print(c)
for i in process_list:
    print(i)