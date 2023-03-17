import sys

def go(index, start, n, m):
    if index == m:
        sys.stdout.write(" ".join(map(str, answer)) + "\n")
        return
    for i in range(start, n):
        answer[index] = nums_list[i]
        go(index + 1, i, n, m)
        
n, m = map(int, input().split())
nums_list = list(map(int, input().split()))
nums_list.sort()
answer = [0] * m

go(0, 0, n, m)