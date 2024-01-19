def is_valid(passcode):
    is_valid = True
    digit_counter = 0
    if not (6 <= len(passcode) <= 10):
        print('Password must be between 6 and 10 characters')
        is_valid = False
    for char in passcode:
        if char.isalpha():
            pass
        elif char.isdigit():
            digit_counter += 1
        else:
            print('Password must consist only of letters and digits')
            return

    if digit_counter < 2:
        print('Password must have at least 2 digits')
        is_valid = False

    if is_valid:
        print('Password is valid')

password = input()
is_valid(password)
