key = int(input())
number_of_iterations = int(input())
string = ''
for _ in range(number_of_iterations):
    user_input = input()
    user_input = ord(user_input)
    user_input += key
    string += chr(user_input)
print(string)