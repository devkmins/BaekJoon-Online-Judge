# https://gabii.tistory.com/entry/BaekJoonPython3-%EB%B0%B1%EC%A4%80-1924%EB%B2%88-2007%EB%85%84

day = 0

daysList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]

m, d = map(int, input().split())

for i in range(m - 1):
    day = day + daysList[i]
    
day = (day + d) % 7

print(weekList[day])