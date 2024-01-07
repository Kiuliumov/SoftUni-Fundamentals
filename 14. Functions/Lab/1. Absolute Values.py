given_numbers = input()
given_numbers = given_numbers.split()
result = [abs(float(x)) for x in given_numbers]
print(result)