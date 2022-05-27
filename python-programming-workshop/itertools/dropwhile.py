
#Python program that uses dropwhile, itertools

import itertools

values = ["cat", "dog", "turnip", "carrot", "fish"]

#print(values)
# Drop values while they are less than length 3.
#result = itertools.dropwhile(lambda s: s.startswith("c"), values)
#for value in result:
#    print(value)

lambda x: x.startswith("c")

result = itertools.filterfalse(lambda s: len(s) <= 3, values)
print(values)
for value in result:
    print(value)

#result = itertools.takewhile(lambda s: len(s) <= 3, values)
#for value in result:
#    print(value)
