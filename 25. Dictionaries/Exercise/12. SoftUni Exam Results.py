language_submissions = {}
results = {}
data = input()
while data != 'exam finished':
    data = data.split('-')
    if data[1] == 'banned':
        name = data[0]
        results.pop(name)
    else:
        name, language, score = data
        score = int(score)
        if language not in language_submissions:
            language_submissions[language] = 0
        language_submissions[language] += 1
        if name in results:
            if results[name] > score:
                pass
            else:
                results[name] = score
        else:
            results[name] = score
    data = input()
print('Results:')
for name,score in results.items():
    print(f'{name} | {score}')
print('Submissions:')
for language,count in language_submissions.items():
    print(f'{language} - {count}')