_ = int(input())

L = list(set(map(int, input().split())))

L.sort()

print(*L)

# 입력이 10개인 경우, print(*L) = 11.3, 밑의 코드는 5.4로 시간 차가 큼.

'''
for i in L:
    print(i, end=' ')
print()
'''