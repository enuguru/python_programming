
import itertools

values = [1, 2, 3]

# Get all permutations of the three numbers.
result = itertools.permutations(values, 2)
for value in result:
    print(value)
