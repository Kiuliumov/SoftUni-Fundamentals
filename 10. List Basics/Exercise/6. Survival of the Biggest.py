given_array = sorted([int(x) for x in input().split(' ')])
given_number_to_remove = int(input())
given_array = given_array[:-given_number_to_remove]
print(', '.join([str(x) for x in given_array]))
