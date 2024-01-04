initial_list = input().split('!')
command = input()
while command != 'Go Shopping!':
    command_parts = command.split()
    if command_parts[0] == 'Urgent':
        if command_parts[1] not in initial_list:
            initial_list.insert(0,command_parts[1])
    elif command_parts[0] == 'Unnecessary':
        if command_parts[1] in initial_list:
            initial_list.remove(command_parts[1])
    elif command_parts[0] == 'Correct':
        if command_parts[1] in initial_list:
            initial_index = initial_list.index(command_parts[1])
            initial_list[initial_index] = command_parts[2]
    elif command_parts[0] == 'Rearrange':
        if command_parts[1] in initial_list:
            initial_list.remove(command_parts[1])
            initial_list.append(command_parts[1])

    command = input()
print(', '.join(initial_list))