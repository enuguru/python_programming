

#Python program that converts dictionary

vegetables = {"carrot": 1, "squash": 2, "onion": 4}

# Convert dictionary to list of tuples.
items = list(vegetables.items())

for item in items:
    print(len(item), item)
