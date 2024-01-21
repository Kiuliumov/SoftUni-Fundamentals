coins = 100
energy = 100
events = input().split('|')
for event in events:
    event,value = event.split('-')
    value = int(value)
    if event == 'rest':
        gained_energy:int = None
        if energy + value >= 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            energy += value
            gained_energy = value
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event == 'order':
        if energy > 30:
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
