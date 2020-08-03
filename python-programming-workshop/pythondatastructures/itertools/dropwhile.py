
#Python program that uses dropwhile, itertools

import itertools

values = ["cat", "dog", "turnip", "carrot", "fish"]

# Drop values while they are less than length 3.
result = itertools.dropwhile(lambda s: len(s) <= 3, values)
for value in result:
    print(value)
