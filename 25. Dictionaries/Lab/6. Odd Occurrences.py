words = input().split(' ')
dict_of_words = {}
for word in words:
    word = word.lower()
    if word not in dict_of_words:
        dict_of_words[word] = 0
    else:
        dict_of_words[word] += 1
for word,count in dict_of_words.items():
    if count % 2 != 0:
        print(word,end=' ')