phone_list = input().split(', ')
command = input()
while command != 'End':
    command_parts = command.split(' - ')
    phone = command_parts[1]
    if command_parts[0] == 'Add':
        if phone not in phone_list:
            phone_list.append(phone)
    elif command_parts[0] == 'Remove':
        if phone in phone_list:
            phone_list.remove(phone)
    elif command_parts[0] == 'Bonus phone':
        tokens = command_parts[1].split(':')
        old_phone = tokens[0]
        new_phone = tokens[1]
        if old_phone in phone_list:
            phone_list.insert(phone_list.index(old_phone) + 1,new_phone)
    elif command_parts[0] == 'Last':
        if phone in phone_list:
            phone_list.remove(phone)
            phone_list.append(phone)
    command = input()
print(', '.join(phone_list))

