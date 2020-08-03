
#Python that gets adjacent list elements

# Input list.
elements = [0, 10, 20, 30]

# Use range
for i in range(1, len(elements),1):
    # Get two adjacent elements.
    a = elements[i - 1]
    b = elements[i]

    # Print two elements.
    print(a, b)
