def get_odd_and_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for i in number:
        i = int(i)
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return [even_sum,odd_sum]
given_number = int(input())
num = get_odd_and_even_sum(given_number)
even_sum_of_numbers = num[0]
odd_sum_of_numbers = num[1]
print(f'Odd sum = {odd_sum_of_numbers}, Even sum = {even_sum_of_numbers}')
