S = int(input())

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for _ in range(S):
    vowel_n = 0
    sentence = input()
    sentence_list = sentence.split()
    for word in sentence_list:
        for alpbet in word:
            if alpbet in vowels:
                vowel_n += 1
    cons = (len(sentence) - (len(sentence_list) - 1)) - vowel_n
    print(cons, vowel_n)
