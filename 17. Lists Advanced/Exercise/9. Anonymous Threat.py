import textwrap
strings = input().split()
command = input()
while command != '3:1':
    command,ind,token = command.split(' ')
    ind = int(ind)
    token = int(token)
    string = ''
    if command == 'merge':
        start_index = ind
        end_index = min(token + 1, len(strings))
        merged_string = ''.join(strings[start_index:end_index])
        strings[start_index:end_index] = [merged_string]
    elif command == 'divide':
        ind = min(ind, len(strings) - 1)
        original_string = strings.pop(ind)
        letters_per_part = len(original_string) // token
        divided_parts = textwrap.wrap(original_string, letters_per_part)
        strings[ind:ind] = divided_parts
    command = input()
print(' '.join(strings))