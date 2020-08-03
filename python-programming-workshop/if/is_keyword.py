
#Python that uses is

class Bird:
    pass

# Create two separate objects.
owl = Bird()
parrot = Bird()

# The objects are not identical.
if owl is not parrot:
    print(False, id(owl), id(parrot))

# These objects are identical.
copy = owl
if copy is owl:
    print(True, id(copy), id(owl))
