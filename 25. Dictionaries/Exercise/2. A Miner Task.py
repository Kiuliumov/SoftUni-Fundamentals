inventory = {}
command = input()
while command != 'stop':
    item = command
    quantity = int(input())
    if item not in inventory:
        inventory[item] = quantity
    else:
        inventory[item] += quantity
    command = input()