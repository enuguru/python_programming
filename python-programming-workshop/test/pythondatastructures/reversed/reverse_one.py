
#Python program that uses reversed, sorted

elements = [22, 333, 0, -22, 1000]

# Use a reversed, sorted view: a descending view.
view = reversed(sorted(elements))

# Display our results.
for element in view:
    print(element)
