characters = int(input())
ascii_sum = 0
for _ in range(characters):
    character = input()
    ascii_sum += ord(character)
print(f'The sum equals: {ascii_sum}')