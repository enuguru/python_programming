

from array import array

# New int array.
a = array("i")

# Append three integers.
a.append(100)
a.append(200)
a.append(300)

# Insert an integer at index 1.
a.insert(1, 900)
print(a)

# Remove this element.
a.remove(200)
print(a)

# Count elements with this value.
print(a.count(900))

# Print.
print(a)
