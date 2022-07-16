'''
해결 방법 -
1. 평점은 각각의 (학점 x 성적)의 합 / 전체 학점
'''

T = int(input())

for _ in range(T):
    N = int(input())
    sum_C = 0
    all_G = 0
    for _ in range(N):
        L = input().split()
        C, G = int(L[0]), float(L[1])
        sum_C += C
        all_G += C * G
    print(sum_C, round(all_G / sum_C, 1))