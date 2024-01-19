inventory = {}
materials = input().split(' ')
for i in range(0, len(materials) - 1, 2):
    quantity = int(materials[i])
    item = materials[i + 1].lower()

    if item not in inventory:
        inventory[item] = quantity
    else:
        inventory[item] += quantity

if inventory.get('shards', 0) >= 250:
    print('Shadowmourne obtained!')

if inventory.get('fragments', 0) >= 250:
    print('Valanyr obtained!')

if inventory.get('motes', 0) >= 250:
    print('Dragonwrath obtained!')

for item, quantity in inventory.items():
    print(f'{item}: {quantity}')
