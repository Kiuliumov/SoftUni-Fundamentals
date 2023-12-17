given_string = input()
capitals = []
for i in given_string:
    if not i.islower():
        index_of_i = given_string.index(i)
        capitals.append(index_of_i)
print(capitals)