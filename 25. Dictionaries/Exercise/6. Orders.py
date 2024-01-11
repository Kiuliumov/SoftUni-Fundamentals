command = input()
hashmap = {}
while command != 'buy':
    product_info = command
    product = command.split(' ')
    name,price,quantity = product
    if name not in hashmap:
        hashmap[name] = [price,quantity]
    else:
        current_quantity = hashmap[name][1]
        hashmap[name] = [price,current_quantity + quantity]
    command = input()
for item,final_price in hashmap.items():
    final_price = final_price[0] * final_price[1]
    print(f'{item} -> {final_price:.2f}')
