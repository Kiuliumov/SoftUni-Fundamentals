given_array = input()
given_array = given_array.split(', ')
even_indexes = []
for i in given_array:
    if i % 2 == 0:
        even_indexes.append(given_array.index(i))