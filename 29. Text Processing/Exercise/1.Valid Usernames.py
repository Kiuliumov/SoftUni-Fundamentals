import re


def is_valid(username):
    if re.match("^[a-zA-Z0-9_-]{3,16}$", username):
        return True
    else:
        return False


usernames = input().split(', ')
for name in usernames:
    if is_valid(name):
        print(name)
