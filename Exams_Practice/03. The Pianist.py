n = int(input())
collection = {}
for _ in range(n):
    piece,composer,key = input().split('|')
    collection[piece] = [composer,key]
command = input()
while command != 'Stop':
    command_parts = command.split('|')
    if command_parts[0] == 'Add':
        piece,composer,key = command_parts[1],command_parts[2],command_parts[3]
        if piece not in collection:
            collection[piece] = [composer,key]
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')
    elif command_parts[0] == 'Remove':
        piece = command_parts[1]
        if piece in collection:
            del collection[piece]
            print(f'Successfully removed {piece}!')
        else:
                print(f'Not a valid operation! {piece} does not exist in the collection.')
    elif command_parts[0] == 'ChangeKey':
        piece,new_key = command_parts[1],command_parts[2]
        if piece in collection:
            collection[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Not a valid operation! {piece} does not exist in the collection.')
    command = input()
for piece,piece_data in collection.items():
    composer,key = piece_data
    print(f'{piece} -> Composer: {composer}, Key: {key}')
