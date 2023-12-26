wagons = '0' * int(input())
wagons = list(map(lambda x: int(x), wagons))
while True:
    command = input()
    if command == 'End':
        print(wagons)
        break
    tokens = command.split(' ')
    if tokens[0] == 'add':
        people_to_add = int(tokens[1])
        wagons[-1] += people_to_add
    elif tokens[0] == 'insert':
        index_to_insert = int(tokens[1])
        people_to_insert = int(tokens[2])
        wagons[index_to_insert] += people_to_insert
    elif tokens[0] == 'leave':
        index_to_deduct = int(tokens[1])
        people_to_deduct = int(tokens[2])
        wagons[index_to_deduct] -= people_to_deduct