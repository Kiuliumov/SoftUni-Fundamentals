given_array = list(map(int, input().split()))
command = input()

def swap(list1, index_1, index_2):
    list1[index_1], list1[index_2] = list1[index_2], list1[index_1]
    return list1

def multiply(list1, index_1, index_2):
    multiplied_value = list1[index_1] * list1[index_2]
    list1[index_1] = multiplied_value
    return list1

def decrease(list1):
    for i in range(len(list1)):
        list1[i] -= 1
    return list1

while command != 'end':
    command_parts = command.split()
    if command_parts[0] == 'swap':
        given_array = swap(given_array, int(command_parts[1]), int(command_parts[2]))
    elif command_parts[0] == 'multiply':
        given_array = multiply(given_array, int(command_parts[1]), int(command_parts[2]))
    elif command == 'decrease':
        given_array = decrease(given_array)
    command = input()
given_array1 = str(given_array)
print(given_array1[1:-1])
