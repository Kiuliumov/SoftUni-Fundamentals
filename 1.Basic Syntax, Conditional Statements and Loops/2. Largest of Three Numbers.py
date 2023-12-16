user_input1 = int(input())
user_input2 = int(input())
user_input3 = int(input())
if user_input1 > user_input2 and user_input1 > user_input3:
    print(user_input1)
elif user_input2 > user_input1 and user_input2 > user_input3:
    print(user_input2)
elif user_input3 > user_input2 and user_input3 > user_input1:
    print(user_input3)
