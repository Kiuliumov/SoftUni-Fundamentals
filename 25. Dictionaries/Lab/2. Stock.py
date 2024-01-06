user_input = input().split(' ')
needed_products = input().split(' ')
products = {}
for i in range(0, len(user_input), 2):
    key = user_input[i]
    value = user_input[i + 1]
    products[key] = int(value)
for j in needed_products:
    if j in products:
        print(f'We have {products[j]} {j} left ')
    else:
        print(f"Sorry,we don't have {j} left.")
