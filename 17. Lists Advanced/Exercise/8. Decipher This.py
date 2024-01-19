words = input().split(' ')
final_sentence = ''
for word in words:
    word = list(word)
    secret_letter = ''
    while word[0].isdigit():
        secret_letter += word[0]
        word.remove(word[0])
    secret_letter = chr(int(secret_letter))
    word.insert(0,secret_letter)
    word[1],word[-1] = word[-1],word[1]
    word.append(' ')
    final_sentence += ''.join(word)
print(final_sentence.strip())