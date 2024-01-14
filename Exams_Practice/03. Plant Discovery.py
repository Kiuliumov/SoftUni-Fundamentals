n = int(input())
plant_data = {}
for _ in range(n):
    data = input().split('<->')
    plant_name, plant_rarity = data[0], int(data[1])
    plant_data[plant_name] = [plant_rarity, []]
command = input()
while command != 'Exhibition':
    command, rest = command.split(': ')
    if command == 'Rate':
        plant, rating = rest.split(' - ')
        if plant not in plant_data:
            print('error')
        else:
            plant_data[plant][1].append(int(rating))
    elif command == 'Update':
        plant, new_rarity = rest.split(' - ')
        if plant not in plant_data:
            print('error')
        else:
            plant_data[plant][0] = int(new_rarity)
    elif command == 'Reset':
        plant = rest
        if plant not in plant_data:
            print('error')
        else:
            if plant not in plant_data:
                print('error')
            else:
                plant_data[plant][1] = []
    command = input()
print('Plants for the exhibition:')
for plant_name, data_list in plant_data.items():
    rarity = data_list[0]
    ratings = data_list[1]
    if ratings:
        average_rating = sum(ratings) / len(ratings)
    else:
        average_rating = 0
    print(f'- {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}')