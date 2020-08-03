

# Correct design of the class should use an instance variable instead:

class Dog:

    def __init__(self, name):  # this is the constructor for the class
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)
['play dead']
