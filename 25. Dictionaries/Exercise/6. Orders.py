command = input()
dictionary = {}
while command != 'buy':
    product_info = command
    product = command.split(' ')
    name,price,quantity = product
    if name not in dictionary:
        dictionary[name] = [price, quantity]
    else:
        current_quantity = dictionary[name][1]
        dictionary[name] = [price, current_quantity + quantity]
    command = input()
for item,final_price in dictionary.items():
    final_price = final_price[0] * final_price[1]
    print(f'{item} -> {final_price:.2f}')
