


#Python program that uses string find

value = "cat picture is cat picture"

# Find first index of this string.
i = value.find("picture")
print(i)

# Find first index (of this string) after previous index.
b = value.find("picture", i + 1)
print(b)
