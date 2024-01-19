def get_even(x):
    return x % 2 == 0
numbers_list = input().split(' ')
numbers_list = list(map(int, numbers_list))
result = list(filter(get_even, numbers_list))
print(result)
