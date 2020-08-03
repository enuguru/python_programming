
# ooohh cool, i did not know this way, very nice
# no comments, the program is much better than the one
# I did

#create a deck of cards and shuffle it using a list

import random

cardList = []
for i in range(1,14) :
    cardList.append("Club"+str(i))
    cardList.append("Diamond"+str(i))
    cardList.append("Heart"+str(i))
    cardList.append("Spade"+str(i))

print("original pack...")
print(cardList)

print("after shuffling the pack...")
random.shuffle(cardList)
print(cardList)
