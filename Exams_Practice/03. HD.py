user_input = input().split('@')
houses = [int(x) for x in user_input]
current_house_position = 0
while True:
    command = input()
    if command == 'Love!':
        break
    else:
        jump_command = int(command.split()[1])
        current_house_position += jump_command
        if current_house_position >= len(user_input):
            current_house_position = 0
        houses[current_house_position] -= 2
        if houses[current_house_position] == 0:
            print(f"Place {current_house_position} has Valentine's day.")
        elif houses[current_house_position] < 0:
            print(f"Place {current_house_position} already had Valentine's day.")
new_list = [x for x in houses if x > 0]
print(f"Cupid's last position was {current_house_position}.")
if len(new_list) == 0:
    print('Mission was successful.')
else:
   print(f"Cupid has failed {len(new_list)} places.")