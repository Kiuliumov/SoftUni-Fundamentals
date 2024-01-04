input1 = int(input())
input2 = int(input())
input3 = int(input())
students_count = int(input())
x = input1 + input2 + input3
counter = 0
while students_count > 0:
    students_count -= x
    counter += 1
    if counter % 4 == 0:
        counter += 1
print(f'Time needed: {counter}h.')
