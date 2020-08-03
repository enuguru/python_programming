

#Python that tests values for true or false

# An empty class for testing.
class Box:
    pass

# Some values to test.
values = [-1, 0, 1, None, Box(), []]

# See if the values are treated as "true" or "false".
for value in values:
    if value: print("True ", end="")
    else: print("False", end="")

    # Display value.
    print("... ", value)
