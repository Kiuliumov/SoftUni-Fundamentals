given_array_of_names = input()
given_array_of_names = given_array_of_names.split(', ')
given_array_of_names = sorted(given_array_of_names,key = lambda x:(-len(x), x))
print(given_array_of_names)