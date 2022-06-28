N = int(input())

money_list = []

for _ in range(N):
    dice = list(map(int, input().split()))

    for num in dice:
        if dice.count(num) == 3:
            money = 10000 + num * 1000
            money_list.append(money)
        elif dice.count(num) == 2:
            money = 1000 + num * 100
            money_list.append(money)
        else:
            money = max(dice) * 100
            money_list.append(money)

print(max(money_list))

        