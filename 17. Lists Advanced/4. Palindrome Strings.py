given_array = input().split(' ')
searched_palindrome = input()
palindromes = []
for i in given_array:
    if i == i[len(i)::-1]:
        palindromes.append(i)
print(palindromes)
print(f'Found palindrome {len([x for x in palindromes if x == searched_palindrome])} times.')