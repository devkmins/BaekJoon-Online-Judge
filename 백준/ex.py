'''
n = int(input())
r = 0
p = 0
q = " "

for i in range(n):
    r += 1
    p = r * "*"
    print(p)
'''
'''
N, M = map(int, input().split(" "))
cards = input().split(" ")
cards = list(map(int, cards))  # card 배열에 있는 것을 죄다 int로 바꿈.
moum = []
for a in range(0, N-1):
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N - 1):
            # or >= m 으로 하고 print(min(moum))
            if cards[a] + cards[b] + cards[c] <= M:
                moum.append(cards[a] + cards[b] + cards[c])

print(max(moum))
'''

'''
from itertools import combinations
N, M = map(int, input().split(" "))
cards = input().split(" ")
cards = list(map(int, cards))
max_num = 0
a = []

for card in combinations(cards, 3):
    card_sum = sum(card)
    if card_sum <= M:
        a.append(card_sum)

print(max(a))
'''
'''
num = int(input())
for i in range(num):
    a = sum(map(int, str(i)))
'''

'''
def factorial(a):
    if a <= 0:
        return 1
    else:
        return a * factorial(a-1)


print(factorial(int(input())))
'''

'''
def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return
    return x


m, M = map(int, input().split(" "))

a = []
for i in range(m, M+1):
    a.append(prime(i))

print(a)
'''

'''
a = []


def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return
    return x


m, M = map(int, input().split(" "))

for i in range(m, M+1):
    a.append(prime(i))

print(a)
'''

'''
a = int(input())

for i in range(1, a+1):
    for j in range(a-i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print("")
'''

# list(map(int, sys.stdin.readline().split()))

'''
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
'''

'''
a = []

input_p = int(input())

score = list(map(int, input().split()))

if input_p == len(score):
    max_s = max(score)
    # a.append(max_s)
    # m_index = score.index(max(score))
    # score.remove(score[m_index])
    for i in score:
        j = i/max_s*100
        a.append(j)

average = sum(a) / len(a)
print(average)
'''

'''
문제

1. 수를 입력받아라.
2. 입력 받은 수가 10보다 작다면 앞에 0을 붙여 두 자리로 만들어라
3. 각 자리의 숫자를 더해라.
4. 입력 받은 수의 오른쪽 자리 수와 더한 값을 붙여라.
5. 처음 입력 받은 수와 같아질 때까지 반복하라.
6. 같아지면, 사이클의 길이를 구해라.

요구사항 정리

1. 수를 입력받아라.
2. 문제처럼 계산하며, 처음 입력 받은 수와 같아질 때까지 반복하라.
3. 사이클 길이를 출력.

설계
input,
if input num < "10"
    "0" + input num
'''

'''
리스트 내포 사용할 것
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)

print(result)

->

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]

lambda도 사용할 것 -> def와 동일한 역할을 한다.
add = lambda a, b: a+b
result = add(3, 4)n o
'''
'''
while

n = input()
c = 0
new = -1

while new != n:
    if int(n) < 10:
        n = n.zfill(2)
    plus = int(n[0]) + int(n[1])
    if plus >= 10:
        plus = str(plus)[1]
    while new != n:
        n = n[1] + str(plus)
        new = n
        c += 1

print(c)
'''
'''
string

words = input().upper()
set_word = list(set(words))
max_word = []

for i in set_word:
    cnt = words.count(i)
    max_word.append(cnt)

if max_word.count(max(max_word)) > 1:
    print('?')
else:
    max_index = max_word.index(max(max_word))
    print(set_word[max_index])

string

group_words = []

input_n = int(input())

c = 0

for i in range(input_n):
    group_words.append(input())

for words in group_words:
    w_count = len(words) - 2
    for word in words:
        w_count -= 1
        if words[(w_count + 1) - w_count] != None:
            if word != words[(w_count + 1) - w_count]:
                c += 1
            else:
                pass
        else:
            pass

print(int(c/len(group_words)))

# if k == j[j.index(k+1):j.index(k+2)]:
# if word == words[words.index(word, w_count, w_count)]:
'''
'''
M, N = int(input()), int(input())
prime_list = []

for num in range(M, N+1):
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
        if error == 0:
            prime_list.append(num)

if len(prime_list) > 0:
    print(sum(prime_list), min(prime_list), sep="\n")
else:
    print(-1)
'''
'''
n1 = 3 * n0

even -> n2 = n1/2
odd -> n2 = (n1+1)/2

n3 = 3*n2
n4 = n3/9(몫)

if even -> n0 = 2*n4
if odd -> n0 = 2*n4 + 1
'''
#n_list = []
# n_list_first = n_list[0]
# n_list_second = n_list[1]
# -> 정렬 후 각각 for문으로 존재하는 지 비교하면 되는데.....
'''
for _ in range(2):
    _ = int(input())
    n = list(map(int, input().split()))
    n_list.append(n)

for i in range(len(n_list)):
    for j in range(len(n_list[i])):
        for k in range()
'''