
#Python program that uses string rfind

value = "cat picture is a good cat picture"

# Get rightmost index of this string.
i = value.rfind("picture")
print(i)

# Get rightmost index within this range of characters.
# ... We search the left four words.
b = value.rfind("picture", 0, i - 1)
print(b)
