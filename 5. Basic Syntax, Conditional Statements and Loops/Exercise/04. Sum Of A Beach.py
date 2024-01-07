given_string = input()
words_to_check = ["sand", "water", "fish", "sun"]
counter = 0
for word in words_to_check:
    occurrences = given_string.lower().count(word)
    counter += occurrences
print(counter)

