all_score = []

for _ in range(5):
    score = sum(list(map(int, input().split())))
    all_score.append(score)

print(all_score.index(max(all_score)) + 1, max(all_score))
