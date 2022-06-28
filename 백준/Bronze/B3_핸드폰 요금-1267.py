N = int(input())
charge = list(map(int, input().split()))

YS, MS = 0, 0

for c in charge:
    YS += (c // 30 + 1) * 10
    MS += (c // 60 + 1) * 15
    print(YS, MS)

if YS < MS:
    print('Y', YS)
elif MS < YS:
    print('M', MS)
else:
    print('Y M', YS)
