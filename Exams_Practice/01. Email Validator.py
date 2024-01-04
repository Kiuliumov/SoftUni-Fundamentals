email = input()
command = input()
while command != 'Complete':
    if command == 'Make Upper':
        email = email.upper()
        print(email)
    elif command == 'Make Lower':
        email = email.lower()
        print(email)
    elif command.startswith('GetDomain'):
        count = int(command.split(' ')[1])
        last_chars = ''
        for i in range(1,count + 1):
            last_chars += email[-i]
        last_chars = last_chars[::-1]
        print(last_chars)
    elif command == 'GetUsername':
        if '@' in email:
            username = ''
            for char in email:
                if char == '@':
                    break
                username += char
            print(username)
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif command.startswith('Replace'):
        character_to_replace = command.split(' ')[1]
        email = email.replace(character_to_replace, '-')
        print(email)
    elif command == 'Encrypt':
        ascii_value = ''
        for char in email:
            ascii_value += str(ord(char)) + ' '
        print(ascii_value)
    command = input()