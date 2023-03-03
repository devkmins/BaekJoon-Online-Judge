N = int(input())
M = int(input())

d = [[0]] + [[1] * (M + 1) for _ in range(N)]

n_cnt = 2
m_cnt = n_cnt + 1

while n_cnt <= N:
    if m_cnt <= M:
        d[n_cnt][m_cnt] = d[n_cnt - 1][m_cnt - 1] + d[n_cnt][m_cnt - 1]
        m_cnt += 1
    else:
        n_cnt += 1
        m_cnt = n_cnt + 1
            
print(d[N][M])