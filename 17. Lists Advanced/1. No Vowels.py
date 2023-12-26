given_array = input()
vowels = ['a', 'o', 'u','e', 'i','A','O','U','E','I']
new_list = [x for x in given_array if x not in vowels]
print(''.join(new_list))