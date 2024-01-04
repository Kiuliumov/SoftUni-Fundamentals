user_input = input().split()
list_of_nums = [int(x) for x in user_input]
all_nums = []
biggest_nums = []
average_sum = sum(list_of_nums) / len(list_of_nums)
for i in list_of_nums:
    if i > average_sum:
        biggest_nums.append(i)
biggest_nums.sort(reverse=True)
if len(biggest_nums) == 0:
    print('No')
elif len(biggest_nums) < 5:
    for k in range(len(biggest_nums)):
        print(biggest_nums[k], end=' ')
else:
    for k in range(5):
        print(biggest_nums[k], end=' ')