
#Python that uses all

items = [False, None, True]

# Some elements evaluate to False, so all is False.
if not all(items):
    print(False)

items = [10, 20, 30]

# All the items evaluate to True.
if all(items):
    print(True)
