number = input()
biggest_num = ''
digits = [int(number[0]),int(number[1]),int(number[2])]
digits.sort(reverse=True)
for i in digits:
    biggest_num += str(i)
print(biggest_num)