import sys

def go(index, n, m, nums_list):
    if index == m:
        sys.stdout.write(" ".join(map(str, answer)) + "\n")
        return
    
    for i in range(n):
        answer[index] = nums_list[i]
        go(index + 1, n, m, nums_list)

n, m = map(int, input().split())
nums_list = list(map(int, input().split()))
nums_list.sort()
answer = [0] * m

go(0, n, m, nums_list)