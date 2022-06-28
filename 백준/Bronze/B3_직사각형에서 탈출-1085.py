x, y, w, h = list(map(int, input().split()))

min_list = [x, y, w-x, h-y]

print(min(min_list))
