judge = {}
command = input()

while command != 'no more time':
    name, contest, points = command.split(' -> ')
    points = int(points)

    if contest not in judge:
        judge[contest] = {}

    if name not in judge[contest]:
        judge[contest][name] = points
    else:
        if judge[contest][name] < points:
            judge[contest][name] = points

    command = input()

for contest in judge:
    i = 1
    print(f'{contest}: {len(judge[contest].keys())} participants')
    current_contest = sorted(judge[contest].items(), key=lambda x: (-x[1], x[0]))
    for name, points in current_contest:
        print(f'{i}. {name} <::> {points}')
        i += 1

print('Individual standings:')
all_students = {}
for data in judge.values():
    for name, points in data.items():
        if name not in all_students:
            all_students[name] = points
        else:
            all_students[name] += points

all_students = sorted(all_students.items(), key=lambda x: (-x[1], x[0]))

i = 1
for student_info in all_students:
    name, points = student_info
    print(f'{i}. {name} -> {points}')
    i += 1

