
#Python program that uses flattened list

def get_element(elements, x, y):
    # Get element with two coordinates.
    return elements[x + (y * 10)]

def set_element(elements, x, y, value):
    # Set element with two coordinates.
    elements[x + (y * 10)] = value

# Create a list of 100 elements.
elements = []
for i in range(0, 100):
    elements.append(0)

i = 0
for x in range(0, 10):
    for y in range(0, 10):
        # Set each element in the list to an incremented number.
        set_element(elements, x, y, i)
        i += 1

# First in first row.
print(get_element(elements, 0, 0))
# Last in first row.
print(get_element(elements, 0, 9))
# First in last row.
print(get_element(elements, 9, 0))
# Last in last row.
print(get_element(elements, 9, 9))
