user_input = input()
sheeps = [i for i in user_input.split(', ')]
sheeps.reverse()
if sheeps[0] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    endangered_sheep = sheeps.index('wolf')
    print(f'Oi! Sheep number {endangered_sheep}! You are about to be eaten by a wolf!')