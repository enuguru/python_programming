

#Repr. This accesses the __repr__ method from a class. Repr stands for 
#"representation." It converts an object into a string representation. 
#Here we display Snake instances in a special way.

#Tip: We return a string from the repr method. The print method automatically 
#calls an object's __repr__ method.

#And: We can call repr to force the __repr__ method to be used. This lets us 
#store the representation string in a variable.

#Python program that uses repr

class Snake:
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return "Snake, type = " + self.type

# Create Snake instance.
# ... Print its repr.
s = Snake("Anaconda")
print(s)

# Get repr of Snake.
value = repr(s)
print(value)
