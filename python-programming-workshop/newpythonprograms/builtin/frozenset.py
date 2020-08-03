

# Strings to put in frozenset.
keys = ["bird", "plant", "fish"]

# Create frozenset.
f = frozenset(keys)
print(f)

# Cannot add to frozenset.
try:
    f.add("cat")
except AttributeError:
    print("Cannot add")

# Can use frozenset as key to dictionary.
d = {}
d[f] = "awesome"
print(d)

