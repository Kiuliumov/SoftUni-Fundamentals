contests = {}
command = input()
while command != 'end of contests':
    contest, password_for_context = command.split(':')
    contests[contest] = password_for_context
    command = input()

data = {}
command = input()
while command != 'end of submissions':
    contest, password, username, points = command.split('=>')
    points = int(points)

    if contest in contests and contests[contest] == password:

        if username not in data:
            data[username] = {contest:points}
        if contest in data[username].keys():
            if data[username][contest] < points:
                data[username][contest] = points
        else:
            data[username][contest] = points
    command = input()
for username, contest_points in data.items():
    data[username] = dict(sorted(contest_points.items(), key=lambda item: item[1],reverse=True))
best_student = max(data, key=lambda name: sum(data[name].values()))
most_points = sum(data[best_student].values())
print(f'Best candidate is {best_student} with total {most_points} points.')
print('Ranking:')
data = dict(sorted(data.items()))
for username,info in data.items():
    print(username)
    for contest,points in info.items():
        print(f'#  {contest} -> {points}')

