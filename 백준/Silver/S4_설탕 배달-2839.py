# 1. n을 5로 나눈 나머지가 0인 경우
    # print(N // 5)
# 2. n을 5로 나눈 나머지가 3으로 나누어 떨어지는 경우
    # print(N // 5 + (N % 5) // 3)
# 3. n을 5로 나눈 나머지가 3으로 나누어 떨어지지 않는 경우
    # 1. 리스트에 5를 뺀 수를 차례대로 담아줌(0보다 큰 경우). ex) 32, 27, 22, 17, 12, 7, 2
    #    여기에서 3으로 나누어 떨어지는 가장 작은 수를 고름.
    #    cnt에는 해당 수의 인덱스를 더해주고, 0이 될 때가지 3을 빼줌.
    # 22 = 17(5) - 12(5) - 9(3) - 6(3) - 3(3) - 0(3)
    # 32 = 27(5) - 22(5) - 17(5) - 12(5) - 9(3) - 6(3) - 3(3) - 0(3)
    # 18 = 13(5) - 8(5) - 3(5) - 0(3)
# 4. n을 3으로 나눈 나머지가 0인 경우
    # print(N // 3)
# 5. n을 3으로 나눈 나머지가 0이 아닐 경우
    # print(-1)

N = int(input())
cnt = 0

if N >= 5 and N % 5 == 0:
    print(N // 5)
    
elif N >= 8 and (N % 5) % 3 == 0:
    print((N // 5) + (N % 5) // 3)
    
elif N >= 8 and (N % 5) % 3 != 0:
    a = [N]
    while N - 5 > 0:
        a.append(N - 5)
        N -= 5
    
    b = [i for i in a if i % 3 == 0]
    min_b = b[-1]
    while min_b - 3 >= 0:
        cnt += 1
        min_b -= 3
    
    print(a.index(b[-1]) + cnt)

elif N >= 3 and N % 3 == 0:
    print(N // 3)
    
else:
    print(-1)

'''
# 위의 코드와 메모리, 시간 사용은 같지만, 훨씬 직관적임.
# 굳이 5를 먼저 뺄 필요 없음.

N = int(input())
cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += (N // 5)
        print(cnt)
        break
    
    N -= 3
    cnt += 1
else:
    print(-1)
'''