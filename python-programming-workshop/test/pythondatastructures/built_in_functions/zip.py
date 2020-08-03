

#Zip built-in. With zip we can act upon two lists at once. Zip() is a built-in function
#We pass it two iterables, like lists, and it enumerates them together.

#Python that uses zip on list

items1 = ["blue", "red", "green", "white"]
items2 = ["sky", "sunset", "lawn", "pillow"]

# Zip the two lists and access pairs together.
for item1, item2 in zip(items1, items2):
    print(item1, "...", item2)
