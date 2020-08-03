
numbers1 = {1, 3, 5, 7} # for set and dictionary we use curly braces. This shows
numbers2 = {1, 3}       # both set and dictionary use a hash key in their implementation

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

numbers3 = {(4,5), "Jayashree", 34.76}
print(numbers3)

mydict = { 23:45, "Karthik G":100000 }
p = (mydict.keys())
print(p)
#numbers3.add(p[1])
#numbers3.add(23)
#print(numbers3)
#numbers3.add([23,45,"Guru"]) #you cannot add a unhashable type like list
#print(numbers3)
