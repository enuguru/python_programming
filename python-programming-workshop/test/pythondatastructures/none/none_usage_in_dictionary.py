

#Python program that uses dictionary, None

items = {"cat" : 1, "dog" : 2, "piranha" : 3}

# Get an element that does not exist.
v = items.get("giraffe")

# Test for it.
if v == None:
    print("Not found")
