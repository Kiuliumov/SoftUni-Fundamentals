numbers = input().split(' ')
command = input()

while command != 'Finish':
    command_parts = command.split(' ')

    if command_parts[0] == 'Add':
        numbers.append(command_parts[1])
    elif command_parts[0] == 'Remove':
        numbers.remove(command_parts[1])
    elif command_parts[0] == 'Replace':
        index = numbers.index(command_parts[1])
        numbers.pop(index)
        numbers.insert(index, command_parts[2])
    elif command_parts[0] == 'Collapse':
        collapse_value = int(command_parts[1])
        new_list = [x if int(x) >= collapse_value else None for x in numbers]
        numbers = [x for x in new_list if x is not None]

    command = input()

numbers = [x for x in numbers if x is not None]
print(' '.join(numbers))
