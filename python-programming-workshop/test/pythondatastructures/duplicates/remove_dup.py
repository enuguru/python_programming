

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

# Remove duplicates from this list.
values = [5, 5, 1, 1, 2, 3, 4, 4, 5]
print(values)
result = remove_duplicates(values)
print(result)
