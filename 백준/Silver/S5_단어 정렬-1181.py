'''
1. 길이가 짧은 것부터 정렬
2. 길이가 같으면 사전 순으로 정렬

입력 -
1. 단어의 개수 N
2. 단어

해결 방법 -
1. 입력을 받은 후, 각 문자의 길이를 key로 두고, 문자를 value로 두는 dictionary를 만든다.
2. 사전 순서대로 정렬 후 길이에 따라 정렬
'''

import string

N = int(input())

dictionary = {}

for _ in range(N):
    word = input()
    dictionary[word] = len(word)
    
dictionary = dict(sorted(dictionary.items()))
    
sorted_dict = dict(sorted(dictionary.items(), key = lambda item: item[1])) # item[1]은 dict의 value를 의미
    
for i in sorted_dict.keys():
    print(i)