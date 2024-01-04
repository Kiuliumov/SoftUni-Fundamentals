given_array = input().split(' ')
command = input()
moves = 0
while command != 'end':
    moves += 1
    command_parts = list(map(lambda x:int(x),command.split(' ')))
    if command_parts[0] == command_parts[1] or command_parts[0] < 0 or command_parts[1] < 0 or command_parts[0] >= len(given_array) or command_parts[1] >= len(given_array):
        middle_index = len(given_array) // 2
        given_array.insert(middle_index, f'-{moves}a')
        given_array.insert(middle_index, f'-{moves}a')
        print('Invalid input! Adding additional elements to the board')
    elif given_array[command_parts[0]] == given_array[command_parts[1]]:
        print(f'Congrats! You have found matching elements - {given_array[command_parts[0]]}!')
        removed_value = given_array[command_parts[0]]
        given_array.remove(removed_value)
        given_array.remove(removed_value)
    elif given_array[command_parts[0]] != given_array[command_parts[1]]:
        print('Try again!')
    if len(given_array) == 0 or len(given_array) == 1:
        print(f'You have won in {moves} turns!')
        break
    command = input()
else:
    print('Sorry you lose :(')
    print(' '.join(map(str,given_array)))
