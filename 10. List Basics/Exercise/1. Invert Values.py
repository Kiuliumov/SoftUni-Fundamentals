given_array = input().split(' ')
given_array = [int(x) for x in given_array]
for i in range(len(given_array)):
    given_array[i] = -i
print(given_array)