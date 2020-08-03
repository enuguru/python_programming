

# Tuple containing unsorted odd numbers.
odds = (9, 5, 11)

# Convert to list and sort.
list = list(odds)
list.sort()
print(list)

# Convert back to tuple.
sorted_odds = tuple(list)
print(sorted_odds)
