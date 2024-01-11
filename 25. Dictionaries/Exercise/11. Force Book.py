force_book = {}
command = input()
while command != 'Lumpawaroo':
    if '|' in command:
        command_parts = command.split(' | ')
        force_side, force_user = command_parts
        user_unique = True
        if force_side not in force_book:
            force_book[force_side] = []
        for side,user in force_book.items():
            if force_user in force_book[side]:
                user_unique = False
        if user_unique:
            force_book[force_side].append(force_user)
    elif '->' in command:
        force_side_exists = False
        is_such_user = False
        command_parts = command.split(' -> ')
        force_user,force_side = command_parts
        if force_side in force_book:
            force_side_exists = True
        for side,user_list in force_book.items():
            if force_user in user_list:
                is_such_user = True
                force_book[side].remove(force_user)
        if is_such_user and force_side_exists:
            force_book[force_side].append(force_user)
        elif not is_such_user and force_side_exists:
            force_book[force_side].append(force_user)
        else:
            force_book[force_side] = []
            force_book[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')
    command = input()
for side,user_list in force_book.items():
    if len(user_list) > 0:
        print(f'Side: {side}, Members: {len(user_list)}')
        for user in user_list:
            print('!' + ' ' + user)


