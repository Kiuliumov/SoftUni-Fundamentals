number_of_iterations = int(input())
capacity = 255
liters = 0
for _ in range(number_of_iterations):
    user_input = int(input())
    if capacity - user_input >= 0:
        capacity -= user_input
        liters += user_input
    else:
        print('Insufficient capacity!')
        continue
print(liters)