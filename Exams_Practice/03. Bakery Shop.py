market = {}
command = input()
sold = 0
while command != 'Complete':
    command_parts = command.split(' ')
    if command_parts[0] == 'Receive':
        quantity = int(command_parts[1])
        food = command_parts[2]
        if food not in market and quantity > 0:
            market[food] = quantity
        elif food in market and quantity > 0:
            market[food] += quantity
    elif command_parts[0] == 'Sell':
        quantity = int(command_parts[1])
        food = command_parts[2]
        if food not in market:
            print(f'You do not have any {food}.')
        elif food in market and market[food] >= quantity:
            market[food] -= quantity
            sold += quantity
            print(f'You sold {quantity} {food}.')
            if int(market[food]) == 0:
                market.pop(food)
        else:
            sold_quantity = market.pop(food)
            sold += sold_quantity
            print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
    command = input()
for food,quantity in market.items():
    print(f'{food}: {quantity}')
print(f'All sold: {sold} goods')
