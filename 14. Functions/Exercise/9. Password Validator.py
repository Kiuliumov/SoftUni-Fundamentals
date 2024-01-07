def is_valid(passcode):
    is_valid = True
    digit_counter = 0
    if len(passcode) < 6 or len(passcode) > 10:
        print('Password must be between 6 and 10 characters')
        is_valid = False
    for i in passcode:
        if 48 <= ord(i) <= 57:
            digit_counter += 1
        if 48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            is_valid = True
        else:
            is_valid = False
            print('Password must consist only of letters and digits')
            break 
    if digit_counter < 2:
        print('Password must have at least 2 digits')
        is_valid = False

    if is_valid:
        print('Password is valid!')
password = input()
is_valid(password)
