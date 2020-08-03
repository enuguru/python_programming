

elements = [0, 200, 50, 25, 10, 255]

# Create bytearray from list of integers.
values = bytearray(elements)

# Modify elements in the bytearray.
values[0] = 5
values[1] = 0

# Display bytes.
for value in values:
    print(value)

