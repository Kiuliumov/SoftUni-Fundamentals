given_string = input()
new_string = ''
for char in given_string:
    new_string += chr(ord(char) + 3)
print(new_string)