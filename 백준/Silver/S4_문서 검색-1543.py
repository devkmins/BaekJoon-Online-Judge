'''
해결 방법 -
입력 받은 문서에 문자를 대조, ababababa이면 aba를 여러 번 대조하며, 일치할 경우 +1 
Slicing을 사용할 것.
'''

a = input()
b = input()

count, index = 0, 0

for i in range(len(a)):
    if index > i:
        continue
    if b == a[i:i + len(b)]:
        count += 1
        index = i + len(b)
        
print(count)