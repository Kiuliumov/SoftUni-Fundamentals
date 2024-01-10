students = []
course_to_search = None
while True:
    student_info = input()
    if ':'  not in student_info:
        course_to_search = student_info
        break
    else:
        name, ID, course = student_info.split(':')
        students.append({'name': name,'ID': ID,'course': course})
        for student in students:
            if student[course] == course_to_search:
                print(f'{student[name]} - {student[ID]}')
