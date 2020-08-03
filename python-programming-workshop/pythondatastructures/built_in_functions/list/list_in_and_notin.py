

items = ["book", "computer", "keys", "mug"]

if "computer" in items:
    print(1)

if "atlas" in items:
    # This is not reached.
    print(2)
else:
    print(3)

if "marker" not in items:
    print(4)
