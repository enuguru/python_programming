
# karthick it produces only one answer, we have to 
# simulate for all values, from 1 to 12, am i right?
# we have to what the PD says and we get, and compare them


#simulate rolling two dice many times and compare the results to the one from probability theory

import random

def dice_roll():
    return random.randint(1, 6)

print(str(dice_roll()) + ":" + str(dice_roll()))

