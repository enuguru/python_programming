

def has_duplicates(values):
    # For each element, check all following elements for a duplicate.
    for i in range(0, len(values)):
        for x in range(i + 1, len(values)):
            if values[i] == values[x]:
                return True
    return False

values = [5, 1, 2, 3, 4]

i = has_duplicates(values)
print(i)
