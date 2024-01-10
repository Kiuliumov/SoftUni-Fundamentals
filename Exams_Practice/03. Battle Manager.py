people = {}
command = input()
while command != 'Results':
    command_parts = command.split(':')
    if command_parts[0] == "Add":
        name = command_parts[1]
        health = int(command_parts[2])
        energy = int(command_parts[3])
        if name not in people:
            people[name] = [health,energy]
        else:
            people[name][0] += health
    elif command_parts[0] == 'Attack':
        attacker_name = command_parts[1]
        defender_name = command_parts[2]
        damage = int(command_parts[3])
        if attacker_name in people and defender_name in people:
            people[defender_name][0] -= damage
            people[attacker_name][1] -= 1
            if people[defender_name][0] <= 0:
                print(f'{defender_name} was disqualified!')
                people.pop(defender_name)
            if people[attacker_name][1] <= 0:
                print(f'{attacker_name} was disqualified!')
                people.pop(attacker_name)
    elif command_parts[0] == 'Delete':
        if command_parts[1] == 'All':
            people = {}
        else:
            if command_parts[1] in people:
                people.pop(command_parts[1])
    command = input()
print(f'People count: {len(people)}')
for name,stats in people.items():
    print(f'{name} - {stats[0]} - {stats[1]}')
