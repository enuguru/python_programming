
import itertools

# A list with seven values.
values = [1, 5, 6, 8, 10, 12, 1]

# Take values until one is higher than 9.
result = itertools.takewhile(lambda v: v < 10, values)

for value in result:
    print(value)
