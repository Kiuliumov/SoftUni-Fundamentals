list_of_chars = input().split(', ')
dict_of_chars = {char: ord(char) for char in list_of_chars}
print(dict_of_chars)
