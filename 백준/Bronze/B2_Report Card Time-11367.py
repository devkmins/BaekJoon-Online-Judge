N = int(input())

for _ in range(N):
    name, grade = input().split()
    if int(grade) >= 97:
        grade = 'A+'
    elif int(grade) >= 90:
        grade = 'A'
    elif int(grade) >= 87:
        grade = 'B+'
    elif int(grade) >= 80:
        grade = 'B'
    elif int(grade) >= 77:
        grade = 'C+'
    elif int(grade) >= 70:
        grade = 'C'
    elif int(grade) >= 67:
        grade = 'D+'
    elif int(grade) >= 60:
        grade = 'D'
    elif int(grade) >= 0 and int(grade) < 60:
        grade = 'F'
    print(name, grade)
