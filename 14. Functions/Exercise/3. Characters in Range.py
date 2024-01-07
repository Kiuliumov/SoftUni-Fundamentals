def ascii_range(first_char,second_char):
    final_string = ''
    for i in range(ord(first_char) + 1,ord(second_char)):
        i = chr(i)
        final_string += i + ' '
    return final_string
charracter1 = input()
charracter2 = input()
result = ascii_range(charracter1,charracter2)
print(result)
