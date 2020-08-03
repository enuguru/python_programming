


#We can initialize attributes of a type with a dictionary argument. This is 
#the third argument. Here I set the attribute "paws" to 4, and "weight" to -1. 
#We display these values on a Cat instance.

#Tip:This is a dictionary instance. It can be created like any other dictionary.
#Dictionary

#Python program that uses dict in type

# Create class type with default attributes (fields).
Cat = type("Cat", (object,), {"paws": 4, "weight": -1})
cat = Cat()

# Access attributes.
print("Paws =", cat.paws)
print("Weight =", cat.weight)
