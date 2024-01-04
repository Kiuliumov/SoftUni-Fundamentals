all_rooms = input().split('|')
health = 100
bitcoins = 0
for i in range(len(all_rooms)):
    current_room = all_rooms[i].split()
    entity = current_room[0]
    if entity == 'potion':
        healed_for = int(current_room[1])
        health += healed_for
        if health > 100:
            healed_for -= health - 100
            health = 100
        print(f'You healed for {healed_for} hp.')
        print(f'Current health: {health} hp.')
    elif entity == 'chest':
        bitcoins += int(current_room[1])
        print(f'You found {current_room[1]} bitcoins.')
    else:
        health -= int(current_room[1])
        if health > 0:
            print(f'You slayed {entity}.')
        else:
            print(f'You died! Killed by {entity}.')
            print(f'Best room: {i + 1}')
            break
else:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
