command = input()
while command != 'End':
    if command != 'SoftUni':
        new_word = ''
        for i in command:
            new_word += i * 2
        print(new_word)
    command = input()