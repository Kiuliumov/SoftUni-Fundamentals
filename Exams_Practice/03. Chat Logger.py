chat_logs = []
command = input()
while command != 'end':
    command = command.split(' ')
    if command[0] == 'Chat':
        message = command[1]
        chat_logs.append(message)
    elif command[0] == 'Delete':
        message = command[1]
        if message in chat_logs:
            chat_logs.remove(message)
    elif command[0] == 'Edit':
        message = command[1]
        edited_version = command[2]
        if message in chat_logs:
            index = chat_logs.index(message)
            chat_logs[index] = edited_version
    elif command[0] == 'Pin':
        message = command[1]
        if message in chat_logs:
            chat_logs.remove(message)
            chat_logs.append(message)
    elif command[0] == 'Spam':
        for message in range(1,len(command)):
            chat_logs.append(command[message])
    command = input()
for message in chat_logs:
    print(message)
