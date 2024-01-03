given_array = input().split('#')
water = int(input())
total_fire = 0
total_effort = 0
cells = []
for i in given_array:
    is_valid = False
    fire_list = i.split(' = ')
    types_of_fire = fire_list[0]
    value_of_the_cell = int(fire_list[1])
    if water < value_of_the_cell:
        continue
    if types_of_fire == 'High' and 80 < value_of_the_cell <= 125:
        is_valid = True
    elif types_of_fire == 'Medium' and 50 < value_of_the_cell <= 80:
        is_valid = True
    elif types_of_fire == 'Low' and 0 < value_of_the_cell <= 50:
        is_valid = True
    if is_valid:
        water -= value_of_the_cell
        cells.append(value_of_the_cell)
        total_fire += value_of_the_cell
        total_effort += 0.25 * value_of_the_cell
print('Cells:')
for j in cells:
    print(f' - {j}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')