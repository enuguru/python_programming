

# As discussed in A Word About Names and Objects, shared data can have possibly 
# surprising effects with involving mutable objects such as lists and dictionaries. 
# For example, the tricks list in the following code should not be used as a 
# class variable because just a single list would be shared by all Dog instances:

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)                # unexpectedly shared by all dogs
