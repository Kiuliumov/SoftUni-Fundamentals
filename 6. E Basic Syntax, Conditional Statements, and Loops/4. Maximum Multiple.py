divisor = int(input())
boundary = int(input())
largest_num = 0
for i in range(1, boundary + 1):
    if i % divisor == 0 and i >= largest_num:
        largest_num = i
print(largest_num)