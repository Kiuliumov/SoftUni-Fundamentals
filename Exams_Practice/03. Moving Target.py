targets = input().split(' ')
targets = [int(x) for x in targets]
command = input()

def shoot(targets_list,ind,power):
    if 0 <= ind < len(targets_list):
        targets_list[ind] -= power
        if targets[ind] <= 0:
            targets_list.remove(targets_list[ind])
def add(targets_list,ind,value):
    if 0 <= ind < len(targets_list):
        targets_list.insert(ind,value)
    else:
        print('Invalid placement!')
def strike(targets_list,ind,radius):
    if 0 <= ind + radius < len(targets_list) and ind - radius >= 0:
        for i in range(ind - radius,ind + radius + 1):
            targets_list[i] = None
    else:
        print('Strike missed!')
while command != 'End':
    command_parts = command.split(' ')
    if command_parts[0] == 'Shoot':
        shoot(targets,int(command_parts[1]),int(command_parts[2]))
    elif command_parts[0] == 'Add':
        add(targets,int(command_parts[1]),int(command_parts[2]))
    elif command_parts[0] == 'Strike':
        strike(targets,int(command_parts[1]),int(command_parts[2]))
        targets = [x for x in targets if x is not None]
    command = input()
targets = [str(x) for x in targets]
print('|'.join(targets))
