N = int(input())
charge = list(map(int, input().split()))

YS, MS = 0, 0

for c in charge:
    YS += c // 30 * 10 + 10
    MS += c // 60 * 15 + 15

if YS < MS:
    print('Y', YS)
elif MS < YS:
    print('M', MS)
else:
    print('Y M', YS)