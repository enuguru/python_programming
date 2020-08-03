

#Make method. Namedtuple offers extra methods—one of them is _make. With _make() 
#we create a namedtuple from an iterable (like a list). The list elements are turned into tuple fields.

#Tip: The make method fills namedtuple fields based on the order of the list's elements. 
#So we must be careful with ordering.

#List

#Python program that uses _make method

import collections

# A namedtuple type.
Style = collections.namedtuple("Style", ["color", "size", "width"])

# A list containing three values.
values = ["red", 10, 15]

# Make a namedtuple from the list.
tuple = Style._make(values)
print(tuple)
