def is_same_when_reversed(num):
    num = list(num)
    reversed_num = list(reversed(num))
    if num == reversed_num:
        return True
    else:
        return False
    
numbers = input().split(', ')
for i in numbers:
    if is_same_when_reversed(i):
        print(True)
    else:
        print(False)
    