'''
해결 방법 -
1. 1부터 N까지 각각의 수들을, 각 수로 쪼개어 공차가 같은지 확인해야 함.
2. 입력이 1000보다 작거나 같기에, if ns[0] - ns[1] == ns[1] - ns[2]와 같이 표현도 가능
'''

def hansu(N):
    c = 0
    for i in range(1, N+1):
        if i < 10:
            c += 1
        else:
            i = str(i)
            d = int(i[1]) - int(i[0])
            cont = 0
            for j in range(len(i) - 1):
                iter_d = int(i[j+1]) - int(i[j])
                if d != iter_d:
                    break
                else:
                    cont += 1
            if cont == len(i) - 1:
                c += 1      
    return c

N = int(input())
print(hansu(N))
        