def add(number1: float,number2: float) -> float:
    return number1 + number2
def subtract(number1: float,number2: float) -> float:
    return number1 - number2
def multiply(number1: float,number2: float) -> float:
    return number1 * number2
def divide(number1: float,number2: float) -> float:
    return number1 / number2
def exponentiation(number1: float,number2: float) -> float:
    return number1 ** number2
def menu():
 print('1. Add two numbers')
 print('2. Subtract two numbers')
 print('3. Multiply two numbers')
 print('4. Divide two numbers')
 print('5. Exponentiation')
 print('6. Quit')
menu()
command = float(input('Enter your command: '))
while command != 6:
    number1 = float(input('Enter your first number: '))
    number2 = float(input('Enter your second number: '))
    if command == 1:
        result = add(number1,number2)
        print(f'Your result is: {result:.2f}')
    elif command == 2:
        result = subtract(number1,number2)
        print(f'Your result is: {result:.2f}')
    elif command == 3:
        result = multiply(number1,number2)
        print(f'Your result is: {result:.2f}')
    elif command == 4:
        result = divide(number1,number2)
        print(f'Your result is: {result:.2f}')
    elif command == 5:
        result = exponentiation(number1, number2)
        print(f'Your result is: {result:.2f}')
    command1 = input('Do you want to continue? y/n: ')
    if command1 == 'y':
        menu()
        command = float(input('Enter your command: '))
    else:
        print('You quit the calculator!')
        break
else:
    print('You quit the calculator!')
