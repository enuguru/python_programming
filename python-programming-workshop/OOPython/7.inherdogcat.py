
# this program shows that the constructor of the base class
# has to be called by the derived class explicitly otherwise
# base class attributes are not initialized
# this program also shows the relationship between derived class
# attributes and functions with base class attributes and functions

class Pet(object):
    
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Pet):
    
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats


class Cat(Pet):
    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs


mypet = Cat('super','yes')
print(mypet.name)
print(mypet.hates_dogs)
print(mypet.__str__())
print(mypet.getName())
print(mypet.getSpecies())
