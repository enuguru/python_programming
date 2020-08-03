
# no problem siva, the solution neat and clean
def new_deck():
    suits = ["spade","diamond","clubs","hearts"]
    ranks = [i for i in range(14) if i > 0]

    deck = list()
    for i in suits:
        for j in ranks:
            deck.append((i,j))
    return deck

deck1 = new_deck()
deck2 = new_deck()

two_decks = deck1 + deck2

picture_cards = (len([a_card for a_card in two_decks if a_card[1] > 10]))

print("Probability of getting a picture card : %d out of %d"%(picture_cards,len(two_decks)) )
