order = input()
quantity = int(input())
def calculate(price: float,quantity: int):
    return price * quantity
if order == 'coffee':
    result = calculate(1.5,quantity)
elif order == 'water':
    result = calculate(1,quantity)
elif order == 'coke':
    result = calculate(1.4,quantity)
elif order == 'snack':
    result = calculate(2,quantity)
print(result)