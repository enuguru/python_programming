
#Dictionary literals

# Method 1

#Perhaps the most commonly used way of constructing a python dictionary is with 
#curly bracket syntax:

d1 = {"age":25}
print(d1)


# Method 2

#As dictionaries are mutable, you need not know all the entries in advance:
# Empty dict

d2 = {}
# Fill in the entries one by one
d2["name"] = "Jayashree"
print(d2)


# Method 3

#From a list of tuples

#You can also construct a dictionary from a list (or any iterable) of 
#key, value pairs. For instance:

	
d3 = dict([("age", 25)])
print(d3)


# Method 4

#This is perhaps most useful in the context of a list comprehension:
	
class Person(object):
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
 
people = [Person("Nick", "Programmer"), Person("Alice","Engineer")]
professions = dict([ (p.name, p.profession) for p in people ])
print(professions)
#{"Nick": "Programmer", "Alice": "Engineer"}


# Method 5

#From two parallel lists

#This method of constructing a dictionary is intimately related to the prior example. 
#Say you have two lists of elements, perhaps pulled from a database table:
	
# Static lists for purpose of illustration
names = ["Nick", "Alice", "Kitty"]
professions = ["Programmer", "Engineer", "Art Therapist"]

#If you wished to create a dictionary from name to profession, you 
#could do the following:
	
professions_dict = {}
for i in range(len(names)):
    professions_dict[names[i]] = professions[i]
print(professions_dict)

#This is not ideal, however, as it involves an explicit iterator, and is 
#starting to look like Java. The more Pythonic way to handle this case would 
#be to use the zip method, which combines two iterables:


print(zip(range(5), ["a","b","c","d","e"]))
 
names_and_professions = zip(names, professions)
print(names_and_professions)
 
for name, profession in names_and_professions:
    professions_dict[name] = profession

#As you can see, this is extremely similar to the previous section. You can 
#dispense the iteration, and instead use the dict method:
	
professions_dict = dict(names_and_professions)
# You can dispence the extra variable and create an anonymous
# zipped list:
professions_dict = dict(zip(names, professions))
print(professions_dict)
