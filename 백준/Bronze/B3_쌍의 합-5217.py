t = int(input())

for test in range(t):
    n = int(input())
    n_list = []
    for i in range(1, 13):
        for j in range(1, 13):
            if i < j:
                if i + j == n:
                    n_list.append(f'{i} {j}')
    for k in range(len(n_list)):
        print(f'Pairs for {n}: {n_list}')