

elements = [False, None, "Pomegranate", 0]

# One value is True, so any returns True.
if any(elements):
    print(True)

elements = [0, 0, False]

# Now no elements are True.
# ... Any returns False.
if not any(elements):
    print(False)
