

# Cities.
names = ["San Jose", "San Francisco", "Santa Fe", "Houston"]

# Sum result of map.
count = sum(map(lambda s: s.startswith("San"), names))

# Count of cities starting with San.
print(count)
