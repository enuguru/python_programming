
numbers1 = {1, 3, 5, 7}
numbers2 = {1, 3}

# Is subset
if numbers2.issubset(numbers1):
    print("Is a subset")

# Is superset
if numbers1.issuperset(numbers2):
    print("Is a superset")

# Intersection of the two sets
print("numbers1 intersection numbers2",numbers1.intersection(numbers2))

print("numbers1 union numbers2",numbers1.union(numbers2))
print("numbers1 difference numbers2",numbers1.difference(numbers2))
print("numbers1 difference numbers2",numbers1.symmetric_difference(numbers2))
