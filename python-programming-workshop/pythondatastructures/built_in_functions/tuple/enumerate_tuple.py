

values = ["meow", "bark", "chirp"]

# Use enumerate on list.
for pair in enumerate(values):
    # The pair is a 2-tuple.
    print(pair)

# Unpack enumerate's results in for-loop.
for index, value in enumerate(values):
    # We have already unpacked the tuple.
    print(str(index) + "..." + value)
