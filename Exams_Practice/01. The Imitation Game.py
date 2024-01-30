given_string = list(input())
command = input()
while command != 'Decode':
    command_parts = command.split('|')
    if command_parts[0] == 'Move':
        number_of_letters = int(command_parts[1])
        for _ in range(number_of_letters):
            given_string.append(given_string.pop(0))
    elif command_parts[0] == 'Insert':
        index,value = command_parts[1],command_parts[2]
        index = int(index)
        given_string.insert(index,value)
    elif command_parts[0] == 'ChangeAll':
        substring,replacement = command_parts[1],command_parts[2]
        current_string = ''.join(given_string)
        if substring in current_string:
            given_string = list(current_string.replace(substring,replacement))
    command = input()
decrypted_message = ''
for item in given_string:
    decrypted_message += item
print(f'The decrypted message is: {decrypted_message}')