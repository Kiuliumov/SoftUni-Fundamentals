positives = []
negatives = []
bound = int(input())
for _ in range(bound):
    number = int(input())
    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)
count_of_positives = len(positives)
sum_of_negatives = sum(negatives)
print(positives)
print(negatives)
print(f'Count of positives: {count_of_positives}')
print(f'Sum of negatives: {sum_of_negatives}')