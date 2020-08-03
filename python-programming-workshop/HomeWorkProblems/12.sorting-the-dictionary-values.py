

# solve the above problem using dictionary

import operator
newdict = {19: 23, 33: 4, 4: 39, 21: 11, 0: 10}
sorted_x = sorted(newdict.items(), key=operator.itemgetter(1))
print(sorted_x)

# if you want to sort dictionary keys
# this is the program

import operator
newdict = {39: 23, 33: 4, 4: 19, 21: 11, 0: 10}
sorted_x = sorted(newdict.items(), key=operator.itemgetter(0))
print(sorted_x)