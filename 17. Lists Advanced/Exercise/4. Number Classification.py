given_nums = input().split(', ')
positive = []
negative = []
even = []
odd = []
for num in given_nums:
    num = int(num)
    if num >= 0:
        positive.append(str(num))
    else:
        negative.append(str(num))
    if num % 2 == 0:
        even.append(str(num))
    else:
        odd.append(str(num))
print('Positive:',', '.join(positive))
print('Negative:',', '.join(negative))
print('Even:',', '.join(even))
print('Odd:',', '.join(odd))