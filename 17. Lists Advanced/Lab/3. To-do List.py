to_do_list = ['0'] * 10
while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-')
    to_do_list.insert(int(tokens[0]),tokens[1])
to_do_list = [x for x in to_do_list if x != '0']
print(to_do_list)