user_input = input().split()
string1 = list(user_input[0])
string2 = list(user_input[1])
result = 0
if len(string1) == len(string2):
    while string1 and string2:
        result += ord(string1.pop(0)) * ord(string2.pop(0))
elif len(string1) > len(string2):
    while string2:
        result += ord(string1.pop(0)) * ord(string2.pop(0))
    for i in string1:
        result += ord(i)
else:
    while string1:
        result += ord(string1.pop(0)) * ord(string2.pop(0))
    for i in string2:
        result += ord(i)
print(result)
