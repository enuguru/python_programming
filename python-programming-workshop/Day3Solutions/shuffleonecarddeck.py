
from random import randrange

def createDeck():
    cards = []
    for suit in ["s", "h", "d", "c"]:
        for value in ["2", "3", "4", "5", "6", "7", "8", \
                      "9", "10", "J", "Q", "K", "A"]:
            cards.append(value + suit)
    return cards


def shuffle(cards):
    for i in range(0, len(cards)):
        other_pos = randrange(0, len(cards))

        temp = cards[i]
        cards[i] = cards[other_pos]
        cards[other_pos] = temp


cards = createDeck()
print(cards)
print()

shuffle(cards)
print(cards)
print()
