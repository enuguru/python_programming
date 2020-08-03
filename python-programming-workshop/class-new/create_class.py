
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def is_old(self):
        return self.age

s = Student('John', 18, "Physics")

print(s.name,s.age,s.major)

print(s.is_old())
