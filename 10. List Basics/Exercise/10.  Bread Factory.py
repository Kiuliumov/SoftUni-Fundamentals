#basic list
coins = 100
energy = 100
events = input().split('|')
for event in events:
    event,value = event.split('-')
    value = int(value)
    if event == 'rest':
        if 100 - energy < value:
            value = 100 - energy
        energy += value
        print(f'You gained {value} energy.')
        print(f'Current energy: {energy}.')
    elif event == 'order':
        if energy >= 30:
            coins += value
            print(f'You earned {value} coins.')
            energy -= 30
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        ingredient = event
        price = value
        if coins >= price:
            coins -= price
            print(f'You bought {ingredient}.')
        else:
            print(f'Closed! Cannot afford {ingredient}.')
            break
else:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')
