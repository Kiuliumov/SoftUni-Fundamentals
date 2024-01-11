courses = {}
while True:
    user_input = input()
    if user_input == 'end':
        break
    student_info = user_input.split(' : ')
    course,name = student_info
    if course not in courses:
        courses[course] = [name]
    else:
        courses[course].append(name)
for course,names in courses.items():
    print(f'{course}: {len(names)}')
    for name in names:
        print(f'-- {name}')