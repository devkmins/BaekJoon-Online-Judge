T = int(input())
d = [[0] * 30 for _ in range(30)]

def bino(n, k):
    if d[n][k]:
        return d[n][k]
        
    if k == 0 or k == n:
        d[n][k] = 1
    else:
        d[n][k] = bino(n - 1, k - 1) + bino(n - 1, k)
        print('d[n][k] ===', d[n][k])
        print('bino(n - 1, k - 1) ===', bino(n - 1, k - 1))
        print('bino(n - 1, k) ===', bino(n - 1, k))
            
    return d[n][k]

for _ in range(T):
    N, M = map(int, input().split())
    print(bino(M, N))