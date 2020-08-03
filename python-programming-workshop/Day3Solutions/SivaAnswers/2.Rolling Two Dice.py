
# you have used list comprehension and dictionary comprehension
# here, which is nice no problem works fine
# you have to roll the dice atleast 100 to 200 times
# in a loop to get probability distribution. right?

import random

dice1 = [i for i in range(7) if i > 0 ]
dice2 = [i for i in range(7) if i > 0 ]

dice2_probability = {i:list() for i in range(13) if i > 0}
print(dice2_probability)

deck = list()
for i in dice1:
    for j in dice2:
        #deck.append((i,str(j)))
        dice2_probability[dice1[i-1]+dice2[j-1]].append((i,j))

print("********** Probability Distribution in Rolling two dices ***********")

for k in dice2_probability:
    print("%d - %d/36 "%(k,len(dice2_probability[k])))
