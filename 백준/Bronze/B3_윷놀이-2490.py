for _ in range(3):
    play_list = list(map(int, input().split()))
    if play_list.count(0) == 1:
        print('A')
    elif play_list.count(0) == 2:
        print('B')
    elif play_list.count(0) == 3:
        print('C')
    elif play_list.count(0) == 4:
        print('D')
    elif play_list.count(0) == 0:
        print('E')
