num = int(input())
total_price = 0
for _ in range(num):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if price_per_capsule == 0 or days == 0 or capsules_needed_per_day == 0:
        continue
    price_for_the_coffee = price_per_capsule * days * capsules_needed_per_day
    print(f'The price for coffee is: ${price_for_the_coffee:.2f}')
    total_price += price_for_the_coffee
print(f'Total: ${total_price:.2f}')