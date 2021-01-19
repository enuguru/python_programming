
class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

p = Person('Pankaj', 34)

print(p.__str__())
print(p.__repr__())
