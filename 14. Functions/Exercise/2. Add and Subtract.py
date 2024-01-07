def sum_of_numbers(num1,num2):
    return num1 + num2
def subtract(result,third_num):
    return result - third_num
def add_and_subtract(first,second,third):
    return subtract(sum_of_numbers(first,second),third)
first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num,second_num,third_num))