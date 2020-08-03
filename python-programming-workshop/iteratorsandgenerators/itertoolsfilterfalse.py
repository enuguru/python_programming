
import itertools

values = ["cat", "parrot", "dog", "bird"]

# Filter out values with length greater than or equal to 4.
result = itertools.filterfalse(lambda e: len(e) >= 4, values)

for element in result:
    print(element)
