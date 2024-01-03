given_first_array = input().split(' ')
is_abandoned = False
seen = []
team_a = 11
team_b = 11
for i in given_first_array:
    if i not in seen:
        tokens = i.split('-')
        if tokens[0] == 'A':
            team_a -= 1
            seen.append(i)
        elif tokens[0] == 'B':
            team_b -= 1
        if team_a < 7 or team_b < 7:
            is_abandoned = True
            break
print(f'Team A - {team_a}; Team B - {team_b}')
if is_abandoned:
    print('Game was terminated')