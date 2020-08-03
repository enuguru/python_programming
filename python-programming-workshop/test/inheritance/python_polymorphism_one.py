
class Dog():
 def __init__(self):
    print("Woof!")
 pass

class Cat():
 def __init__(self):
    print("Meow!")
 pass

class Mammal(Dog, Cat):
 def __init__(self):
    Dog.__init__(self)
 pass

mammal = Mammal()
print(mammal)
