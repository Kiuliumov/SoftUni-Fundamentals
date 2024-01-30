input_string = input()
current_strength = 0
result = []
for char in input_string:
    if char == '>':
        current_strength += int(input_string[input_string.index(char) + 1])
    else:
        if current_strength == 0:
            result.append(char)
        else:
            current_strength -= 1
print("".join(result))
