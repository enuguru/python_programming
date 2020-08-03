

rents = {"apartment": 1000, "house": 1300}

# Convert to list of tuples.
rentItems = rents.items()

# Loop and display tuple items.
for rentItem in rentItems:
    print("Place:", rentItem[0])
    print("Cost:", rentItem[1])
    print("")

print(rentItems)
