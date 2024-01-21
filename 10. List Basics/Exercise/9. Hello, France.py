ticket_cost = 150
items = input().split('|')
budget = int(input())
profit = 0
prices = []
for item in items:
    item,price = item.split('->')
    price = float(price)
    maxprice:float = None
    if item == 'Clothes':
        maxprice = 50
    elif item == 'Shoes':
        maxprice = 35
    elif item  == 'Accessories':
        maxprice = 20.50
    if price > maxprice:
        continue
    elif budget < price:
        continue
    else:
        budget -= price
        prices.append(price + price * 0.4)
        profit += price * 0.4
for item in prices:
    print(f'{item:.2f}',end=' ')
print(f'\nProfit: {profit:.2f}')
if budget + sum(prices) >= ticket_cost:
    print('Hello, France!')
else:
    print('Not enough money.')