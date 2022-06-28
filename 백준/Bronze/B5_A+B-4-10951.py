while True:
    i = input().split()
    a = i[0]
    b = i[1]
    if a or b != " ":
        print(int(a) + int(b))