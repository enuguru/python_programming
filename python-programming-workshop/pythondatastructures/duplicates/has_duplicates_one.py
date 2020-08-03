

def has_duplicates(values):
    # For each element, check all following elements for a duplicate.
    for i in range(0, len(values)):
        for x in range(i + 1, len(values)):
            if values[i] == values[x]:
                return True
    return False

# Test the has_duplicates method.
print(has_duplicates([10, 20, 30, 40]))
print(has_duplicates([1, 2, 3, 1, 2]))
print(has_duplicates([40, 30, 20, 40]))
print(has_duplicates(["cat", "dog", "bird", "dog"]))
print(has_duplicates([None, 0, 1, 2]))
