chars = [x for x in input() if x != ' ']
chars_dict = {}
for char in chars:
    if char not in chars_dict:
        chars_dict[char] = 0
    else:
        chars_dict[char] += 1
for char,count in chars_dict.items():
    print(f'{char} -> {count}')
