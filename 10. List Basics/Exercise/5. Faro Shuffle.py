deck = input().split()
num_shuffles = int(input())
n = len(deck) // 2
shuffled_deck = []

for i in range(n):
    shuffled_deck.append(deck[i])
    shuffled_deck.append(deck[i + n])
for _ in range(num_shuffles):
    deck = shuffled_deck

print(deck)
