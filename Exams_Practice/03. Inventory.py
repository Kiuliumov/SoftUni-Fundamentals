inventory = input().split(', ')
command = input()

def collect(inv,item):
    if item not in inv:
        inv.append(item)

def drop(inv,item):
    if item in inv:
        inv.remove(item)

def combine_items(inv,old_item,new_item):
    if old_item in inv:
        inv.insert(inv.index(old_item) + 1,new_item)

def renew(inv,item):
    if item in inv:
        inv.remove(item)
        inv.append(item)

while command != 'Craft!':
    command_parts = command.split(' - ')
    if command_parts[0] == 'Collect':
        collect(inventory, command_parts[1])
    elif command_parts[0] == 'Drop':
        drop(inventory, command_parts[1])
    elif command_parts[0] == 'Combine Items':
        items = command_parts[1].split(':')
        combine_items(inventory,items[0],items[1])
    elif command_parts[0] == 'Renew':
        renew(inventory,command_parts[1])
    command = input()
print(', '.join(inventory))