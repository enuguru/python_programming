
animals = {}
animals["monkey"] = 1
animals["tuna"] = 2
animals["giraffe"] = 4

# Use in.
if "tuna" in animals:
    print("Has tuna")
else:
    print("No tuna")

# Use in on nonexistent key.
if "elephant" in animals:
    print("Has elephant")
else:
    print("No elephant")
