command = input()
coffee_count = 0
while command != 'END':
    if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        if command.islower():
            coffee_count += 1
        else:
            coffee_count += 2
    else:
        continue
    command = input()

if coffee_count <= 5:
    print(coffee_count)
else:
    print('You need extra sleep!')
