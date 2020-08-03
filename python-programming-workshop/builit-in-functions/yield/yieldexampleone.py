def odds(arg):
    # Yield odd elements in the iterable.
    for a in arg:
        if a % 2 != 0:
            yield a

# An input list.
items = [100, 101, 102, 103, 104, 105]

# Display all odd items.
for item in odds(items):
    print(item)

# Print copied list.
copy = list(odds(items))
print(copy)
