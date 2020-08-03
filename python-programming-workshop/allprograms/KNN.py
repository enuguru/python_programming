
def distance(fruit1, fruit2):
    """
    The args are iterables of the values in the table. 
    for example the args should look something like this:
    
    #         weight,  color
    fruit1 = [303,     3]  # Banana from the data set
    fruit2 = [373,     1]  # the unclassified fruit
    """
    
    # first let's get the distance of each parameter
    a = fruit1[0] - fruit2[0]
    b = fruit1[1] - fruit2[1]
    
    # the distance from point A (fruit1) to point B (fruit2)
    c = (a**2 + b**2) **0.5
    
    return c

# the unknown fruit from above
unknown_fruit = [373, 1]

# This is arbitrarily chosen for this example. Generally
# you need to play with this magic number to find what works
# best for your case

k = 3
# heres the dataset as a python list
dataset = [
  # weight, color, type
  [303, 3, "banana"],
  [370, 1, "apple"],
  [298, 3, "banana"],
  [277, 3, "banana"],
  [377, 4, "apple"],
  [299, 3, "banana"],
  [382, 1, "apple"],
  [374, 4, "apple"],
  [303, 4, "banana"],
  [309, 3, "banana"],
  [359, 1, "apple"],
  [366, 1, "apple"],
  [311, 3, "banana"],
  [302, 3, "banana"],
  [373, 4, "apple"],
  [305, 3, "banana"],
  [371, 3, "apple"],
]

# using the distance() function from above, sort
# the data set by smallest distances on top
sorted_dataset = sorted(dataset, key=lambda fruit: distance(fruit, unknown_fruit))


# from the python std library
from collections import Counter

# take only the first K items
top_k = sorted_dataset[:k]

class_counts = Counter(fruit for (weight, color, fruit) in top_k)

# class_counts now looks like this:
# {"apple": 3}
   
# get the class with the most votes
classification = max(class_counts, key=lambda cls: class_counts[cls])

# There you have it!
classification == "apple"

#e == (a**2 + b**2 + c**2 + d**2) **0.5

#         weight, color, seeds
fruit1 = [303,    3,     1]  # Banana from the data set
fruit2 = [297,    1,     4]  # unknown (but it's an apple)

a = fruit1[0] - fruit2[0]
b = fruit1[1] - fruit2[1]
c = fruit1[2] - fruit2[2]

distance = (a**2 + b**2 + c**2) **0.5
