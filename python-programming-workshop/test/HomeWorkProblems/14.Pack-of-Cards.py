
# Create a pack of cards: 4 suits - ace, hearts, diamond
# and spade, 13 values per suit

import itertools as it

rank_string = ("ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king")
suit_string = ("clubs","diamonds","hearts","spades")

print('The cards are:')
for i, card in enumerate(it.product(rank_string, suit_string)):
    print(i, '{0[1]} of {0[0]}'.format(card))
