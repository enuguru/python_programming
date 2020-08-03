
# looks very good and clean karthick, nice
# probability of a picture card in a two pack

import random

cardList = []
for i in range(1,14) :
    cardList.append("Club"+str(i))
    cardList.append("Diamond"+str(i))
    cardList.append("Heart"+str(i))
    cardList.append("Spade"+str(i))
for i in range(1,14) :
    cardList.append("Club"+str(i))
    cardList.append("Diamond"+str(i))
    cardList.append("Heart"+str(i))
    cardList.append("Spade"+str(i))

print("the two pack card list...")
print(cardList)

print("after shuffling the pack, this is the random card")
random.shuffle(cardList)
# print(cardList)
randomPull = random.sample(cardList, 1)[0]
print(randomPull)

print("probability of getting a picture card from two packs is")
prob = 24/len(cardList)
print(prob)

