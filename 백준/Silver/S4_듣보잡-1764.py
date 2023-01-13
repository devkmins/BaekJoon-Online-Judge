import sys

n, m = map(int, input().split())

n_list = {sys.stdin.readline().rstrip() for _ in range(n)}
m_list = {sys.stdin.readline().rstrip() for _ in range(m)}

same = list(n_list & m_list)
same.sort()

print(len(same))

for i in same:
    print(i)