from collections import deque
given_string = deque(input())
result = deque()
while given_string:
    current_letter = given_string.popleft()
    if result and current_letter == result[-1]:
        continue
    result.append(current_letter)
print(''.join(result))