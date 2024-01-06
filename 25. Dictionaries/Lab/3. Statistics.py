command = input()
products = {}
while command != 'statistic':
    command_parts = input().split(': ')
    product = command_parts[0]
    quantity = command_parts[1]
    if product not in products:
        products[product] = int(quantity)
    command = input()
print('Products in stock:')
for product, quantity in products.items():
    print(f'- {product}: {quantity}')
