

animals = ["cat", "bird", "dog"]

# Use enumerate to get indexes and elements from an iterable.
# ... This unpacks a tuple.
for i, element in enumerate(animals):
    print(i, element)

# Does not unpack the tuple.
for x in enumerate(animals):
    print(x, "UNPACKED =", x[0], x[1])
