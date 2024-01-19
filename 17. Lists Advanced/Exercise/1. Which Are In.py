substrings = input().split(', ')
strings = input().split(', ')
seen = []
for substring in substrings:
    for string in strings:
        if substring in string and substring not in seen :
            seen.append(substring)
print(seen)