n = int(input())
plants = {}
for _ in range(n):
    plants_given = input().split('<->')
    plant_name = plants_given[0]
    plant_values = list(map(float, plants_given[1].split()))
    plants[plant_name] = plant_values
command = input()
while command != 'Exhibition':
    if command.startswith('Rate'):
        command_part, rest = command.split(' ', 1)
        name, value = rest.split(' - ')
        plants[name].append(float(value))
    elif command.startswith('Update'):
        command_part, rest = command.split(' ', 1)
        name, new_value = rest.split(' - ')
        plants[name][0] = float(new_value)
    elif command.startswith('Reset'):
        name = command.split(' ')[1]
        plants[name] = []
    command = input()
for plant_name, plant_values in plants.items():
    rarity = int(plant_values[0]) if plant_values else 0
    if len(plant_values) > 1:
        average_rating = sum(plant_values[1:]) / (len(plant_values) - 1)
        plants[plant_name].append(average_rating)
    else:
        plants[plant_name].append(0.00)
print("Plants for the exhibition:")
for plant_name, plant_values in plants.items():
    rarity = int(plant_values[0]) if plant_values else 0
    print(f'- {plant_name}; Rarity: {rarity}; Rating: {plant_values[2]:.2f}')
