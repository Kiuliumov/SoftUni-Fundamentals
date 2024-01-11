n = int(input())
students = {}
for _ in range(n):
    name = input()
    grade = int(input())
    if name not in students:
        students[name] = []
        students[name].append(grade)
    else:
        students[name].append(grade)
for student_name,grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f'{student_name} -> {average_grade}')