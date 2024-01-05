deck = input().split(', ')
n = int(input())
for _ in range(n):
    command = input().split(', ')
    if command[0] == 'Add':
        card = command[1]
        if card not in deck:
            deck.append(card)
            print('Card successfully added')
        else:
            print('Card is already in the deck')
    elif command[0] == 'Remove':
        card = command[1]
        if card in deck:
            deck.remove(card)
            print('Card successfully removed')
        else:
            print('Card not found')
    elif command[0] == 'Remove At':
        index_of_the_card = int(command[1])
        if 0 <= index_of_the_card < len(deck):
            del deck[index_of_the_card]
            print('Card successfully removed')
        else:
            print('Index out of range')
    elif command[0] == 'Insert':
        index_of_the_card = int(command[1])
        card = command[2]
        if not 0 <= index_of_the_card < len(deck):
            print('Index out of range')
        elif card in deck:
            print('Card is already added')
        else:
            deck.insert(index_of_the_card,card)
            print('Card successfully added')
print(', '.join(deck))
