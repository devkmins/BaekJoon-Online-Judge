'''
해결 방법 -
1. 수첩 2의 숫자를 꺼내, 수첩 1과 비교하며, 있으면 1 출력 없으면 0 출력
'''
N = int(input())

for _ in range(N):
    n1 = int(input())
    note1 = set(map(int, input().split()))
    n2 = int(input())
    note2 = list(map(int, input().split()))
    for i in note2:
        print(1 if i in note1 else 0)
        