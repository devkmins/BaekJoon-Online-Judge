A = input()
time = 0

alphabet_dict = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
                 5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'],
                 8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}

for a in A:
    for key, value in alphabet_dict.items():
        if a in value:
            for t in range(1, key+1):
                if t == 1:
                    time += 2
                else:
                    time += 1

print(time)
