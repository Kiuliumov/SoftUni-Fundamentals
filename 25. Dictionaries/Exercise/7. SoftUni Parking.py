parking = {}
n = int(input())
for _ in range(n):
    command = input().split(' ')
    if command[0].startswith('r'):
        if command[1] not in parking:
            parking[command[1]] = command[2]
            print(f'{command[1]} registered {command[2]} successfully')
        else:
            print(f'ERROR: already registered with plate number {parking[command[2]]}')
    elif command[0].startswith('u'):
        if command[1] not in parking:
            print(f'ERROR: user {command[1]} not found.')
        else:
            removed_user = parking.pop(command[1])
            print(f'{removed_user} unregistered successfully')
for username,license_plate_number in parking.items():
    print(f'{username} => {license_plate_number}')
