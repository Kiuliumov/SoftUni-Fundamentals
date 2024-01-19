user_input = input().split(', ')
numbers = list(map(int, user_input))
nums = {}
current_boundary = 10
while numbers:
    nums[current_boundary] = []
    for number in numbers.copy():
        if number <= current_boundary:
            nums[current_boundary].append(number)
            numbers.remove(number)
    current_boundary += 10
for group, array in nums.items():
    print(f"Group of {group}'s: {array}")
