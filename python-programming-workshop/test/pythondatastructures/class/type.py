


#Python 3 supports classes. With the type built-in, we can directly 
#create types. From these types we can instantiate classes. With setattr 
#we can add attributes (fields) to our classes.

#Example

#This example creates a type with the type built-in. This is an alternative 
#syntax form to the class keyword. We name this type "Cat." It inherits from 
#object, the base class for Python types. And it has no initial attributes.

#Setattr: We use setattr to add a field (or attribute) to our class instance. 
#We pass the class instance, the attribute name, and the value.

#Getattr:Next we call getattr to fetch the value of a class's attribute. 
#Here this call returns the value set by setattr.

#Based on:

#Python 3

#Python program that uses type

Cat = type("Cat", (object,), dict())
cat = Cat()

# Set weight to 4.
setattr(cat, "weight", 10)

# Get the weight.
value = getattr(cat, "weight")
print(value)
