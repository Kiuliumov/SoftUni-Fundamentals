scores_of_all_employees = input()
scores_of_all_employees = scores_of_all_employees.split(' ')
scores_of_all_employees = list(map(lambda x: int(x), scores_of_all_employees))
employees_factor = int(input())
all_employees = len(scores_of_all_employees)
happy_counter = 0

scores_of_all_employees = list(map(lambda x:  x * employees_factor,scores_of_all_employees))
average = sum(scores_of_all_employees) / all_employees


for i in scores_of_all_employees:
    if i >= average:
        happy_counter += 1
if happy_counter >= all_employees/2:
    print(f'Score: {happy_counter}/{all_employees}. Employees are happy!')
else:
    print(f'Score: {happy_counter}/{all_employees}. Employees are not happy!')