cities = {}
command = input()
while command != 'Sail':
    user_input = command.split('||')
    city,population,gold = user_input
    population = int(population)
    gold = int(gold)
    if city not in cities:
        cities[city] = {'population': population,'gold': gold}
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold
    command = input()
command = input()
while command != 'End':
    command = command.split('=>')
    if command[0] == 'Plunder':
        command.pop(0)
        city, people, gold = command
        people = int(people)
        gold = int(gold)
        cities[city]['population'] -= people
        cities[city]['gold'] -= gold
        print(f'{city} plundered! {gold} gold stolen, {people} citizens killed.')
        if cities[city]['population'] == 0 or cities[city]['gold'] == 0:
            cities.pop(city)
            print(f'{city} has been wiped off the map!')
    elif command[0] == 'Prosper':
        command.pop(0)
        city,gold = command
        gold = int(gold)
        if gold >= 0:
            cities[city]['gold'] += gold
            print(f'{gold} gold added to the city treasury. {city} now has {cities[city]["gold"]} gold.')
        else:
            print('Gold added cannot be a negative number!')
    command = input()
if cities:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for city,data in cities.items():
        print(f'{city} -> Population: {data["population"]} citizens, Gold: {data["gold"]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
