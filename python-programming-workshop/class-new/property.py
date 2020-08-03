

#Property. A property gets and sets a value. It is just like a method, 
#but uses simpler syntax. A property can be assigned like a variable. 
#This causes the setter method to be executed.

#Here: We pass two arguments to the property built-in. We specify 
#getname as the getter, and setname as the setter.

#Tip: Any code statements can be used in getters and setters. Here we 
#capitalize the string passed to setname.

#Snake: We create a Snake class instance. Then we assign the "name" 
#property. This invokes the setname method of the Snake class.

#Finally: We print the value of the name property. This invokes the getname method.

#Python that uses property

class Snake:
    def getname(self):
        return self._name

    def setname(self, value):
        # When property is set, capitalize it.
        self._name = value.capitalize()

    name = property(getname, setname)

# Create a snake instance.
s = Snake()

# Set name property.
s.name = "rattle"

# Get name property.
print(s.name)
