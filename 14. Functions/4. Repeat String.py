string = input()
times_to_multiply = int(input())
repeating_string = lambda a, b: a * b
result = repeating_string(string,times_to_multiply)
print(result)