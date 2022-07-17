'''
해결 방법 -
1. 연도를 기준으로 정렬
2. 연도가 같으면, 월과 일을 더한 값이 더 큰 사람이 나이가 적은 것으로 판별
'''

# 다른 사람 코드

import sys

L = []

for _ in range(int(input())):
    n, d, m, y = input().rstrip().split()
    d, m, y = map(int, (d, m, y))
    L.append((y, m, d, n))
    
L.sort()

print(L[-1][3])
print(L[0][3])

# sort를 하면 간단하게 정렬이 됨.

'''
내 코드 -

import sys

n = int(input())

old_people, young_people = '', ''
o_day, o_month, o_year = 32, 13, 9999
y_day, y_month, y_year = 0, 0, 0

for _ in range(n):
    L = sys.stdin.readline().split()
    p_name, p_day, p_month, p_year = L[0], int(L[1]), int(L[2]), int(L[3])
    if p_year > y_year:
        y_year, y_month, y_day = p_year, p_month, p_day
        young_people = p_name
    elif p_year == y_year:
        if p_month > y_month:
            y_year, y_month, y_day = p_year, p_month, p_day
            young_people = p_name
        elif p_month == y_month:
            if p_day > y_day:
                y_year, y_month, y_day = p_year, p_month, p_day
                young_people = p_name
                
    if p_year < o_year:
        o_year, o_month, o_day = p_year, p_month, p_day
        old_people = p_name
    elif p_year == o_year:
        if p_month < o_month:
            o_year, o_month, o_day = p_year, p_month, p_day
            old_people = p_name
        elif p_month == o_month:
            if p_day < o_day:
                o_year, o_month, o_day = p_year, p_month, p_day
                old_people = p_name

print(young_people)
print(old_people)
'''