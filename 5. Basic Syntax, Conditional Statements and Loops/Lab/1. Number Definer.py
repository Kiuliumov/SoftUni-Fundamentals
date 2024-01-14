user_input = input()
if user_input == '0':
    print('zero')
user_input = float(user_input)
if user_input > 0:
    if user_input < 1:
        print('small positive')
    elif user_input > 1000000:
        print('large positive')
    else:
        print('positive')
else:
    user_input = abs(user_input)
    if 0 < user_input < 1:
        print('small negative')
    elif user_input > 1000000:
        print('large negative')
    else:
        print('negative')
