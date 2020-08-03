

#Python that converts bytes, string

# Convert from string to bytes.
value = "carrot"
data = bytes(value, "ascii")
print(data)

# Convert bytes into string with decode.
original = data.decode("ascii")
print(original)
