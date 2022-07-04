'''
해결 방법 -
1. 입력 받은 문자열에 크로아티아 알파벳이 포함되어 있다면, 크로아티아 알파벳을 *로 변환
(크로아티아 알파벳의 길이가 2 이상인 경우도 있으므로, 한 글자로 변환)
2. 문자열의 길이 출력
'''

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
    
print(len(word))