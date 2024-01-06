command = input()
products = {}
while command != 'statistic':
    command_parts = input().split(': ')
    product = command_parts[0]
    quantity = int(command_parts[1])
    if product not in products:
        products[product] = 0
    product[product] += quantity
    command = input()
print('Products in stock:')
for product, quantity in products.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity {sum(products.values())}')
