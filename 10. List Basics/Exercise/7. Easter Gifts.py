gifts = input().split(' ')
command = input()
while command != 'No Money':
    command_parts = command.split(' ')
    if command_parts[0] == 'OutOfStock':
        if command_parts[1] in gifts:
            while command_parts[1] in gifts:
                gifts[gifts.index(command_parts[1])] = None
    elif command_parts[0] == 'Required':
        if 0 <= int(command_parts[2]) < len(gifts):
            gifts[int(command_parts[2])] = command_parts[1]
    elif command_parts[0] == 'JustInCase':
        gifts[-1] = command_parts[1]
    command = input()
arr = [x for x in gifts if x is not None]
print(' '.join(arr))
