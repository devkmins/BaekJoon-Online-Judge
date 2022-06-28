N = int(input())
group = 0

for _ in range(N):
    word = input()
    word_list = []
    for w in word:
        word_list.append(w)
        if w.index == word_list.index(w) + 1:
            break
    group += 1

print(group)
