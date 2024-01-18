def is_perfect_number(num):
    if num <= 0:
        return "It's not so perfect."

    divisor_sum = sum([divisor for divisor in range(1, num) if num % divisor == 0])

    if divisor_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())
result = is_perfect_number(number)
print(result)
