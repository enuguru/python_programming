
original = {"box": 1, "cat": 2, "apple": 5}

# Create copy of dictionary.
modified = original.copy()

# Change copy only.
modified["cat"] = 200
modified["apple"] = 9

# Original is still the same.
print(original)
print(modified)
