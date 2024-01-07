given_array = input()
vowels = ['a', 'o', 'u','e', 'i']
new_list = [x for x in given_array if x.lower() not in vowels]
print(''.join(new_list))