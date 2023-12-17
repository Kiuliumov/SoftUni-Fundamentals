string_1 = input()
string_2 = input()
for i in range(len(string_1)):
    current_string = string_1
    if current_string[i] != string_2[i]:
        current_string = current_string[:i] + string_2[i] + current_string[i + 1:]
        print(current_string)