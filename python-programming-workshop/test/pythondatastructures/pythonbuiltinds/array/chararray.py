

from array import array

# Create a Unicode char array.
a = array("u", "python")

# Display letters in array.
for letter in a:
    print(letter)

# Convert array to a list.
# ... Then join it.
s = "".join(a.tolist())
print(s)
