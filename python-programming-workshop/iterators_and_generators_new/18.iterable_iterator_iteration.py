
for city in ["Berlin", "Vienna", "Zurich"]:
	print(city)

print("\n")

for city in ("Python", "Perl", "Ruby"):
	print(city)

print("\n")

for char in "Iteration is easy":
	print(char, end = " ")

print("\n")

# list of cities
cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
