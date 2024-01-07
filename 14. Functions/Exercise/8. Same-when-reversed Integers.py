def is_same_when_reversed(num):
    reversed_num = reversed(str(num))
    if str(num) == reversed_num:
        return True
    else:
        return False
    
numbers = input().split(', ')
for i in numbers:
    if is_same_when_reversed(i):
        print(True)
    else:
        print(False)
    