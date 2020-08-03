
# perfect this methods is better what I could
# come up with

import random

suits = ["spade","diamond","clubs","hearts"]
ranks = [i for i in range(14) if i > 0]

deck = list()
for i in suits:
    for j in ranks:
        deck.append((i,str(j)))

print("New Deck of cards::",deck)
random.shuffle(deck)
print("Shuffled Deck of cards::",deck)
