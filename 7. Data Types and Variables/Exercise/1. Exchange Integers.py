a = input()
b = input()
print(f'Before: a = {a} b = {b}')
a,b = b,a
print(f'After: a = {a} b = {b}')