
#hash table
plants = {}

# Add three key-value tuples to the dictionary.
plants["radish"] = [2,4,"good"]
plants["squash"] = [1,34,"bad"]
plants["carrot"] = [4,56,"yes"]

print(plants)

# Get syntax 1.
print(plants["radish"])

# Get syntax 2.
print(plants.get("tuna"))
print(plants.get("tuna", "no tuna found"))
print(plants.get('squash'))
sorted(plants)
print(plants)
