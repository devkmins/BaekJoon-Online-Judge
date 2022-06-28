for _ in range(int(input())):
    k = int(input())
    n = int(input())
    people = 0
    if k == 0:
        people = n
        print(people)

    '''
    if k > 1:
        for _ in range(k):
            for _ in range(k):
                for num in range(1, n+1):
                    people += num
    else:
        for _ in range(k):
            people = sum([num for num in range(1, n+1)])
    print(people)
    '''
