given_input = list(input())
while ':' in given_input:
    ind = given_input.index(':')
    print(f':{given_input[ind + 1]}')
    given_input.remove(':')