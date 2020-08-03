

import random

elements = ["cat", "dog", "horse", None, "gerbil"]

def random_element():
    # Return random element from list.
    return random.choice(elements)

# Use iter until a None element is returned.
for element in iter(random_element, None):
    print(element)
