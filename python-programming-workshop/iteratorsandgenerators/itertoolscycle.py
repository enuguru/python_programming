
import itertools

# Cycle through these values.
result = itertools.cycle([1, 2, 3])

# Display first ten results.
i = 0
for value in result:
    print(value)
    i += 1
    if i >= 10:
        break
