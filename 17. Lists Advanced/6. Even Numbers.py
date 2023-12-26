given_array = input()
given_array = given_array.split(', ')
even_indexes = []
for i in given_array:
    i = int(i)
    if i % 2 == 0:
        ind = given_array.index(str(i))
        even_indexes.append(ind)
print(even_indexes)