
# Python program to demonstrate
# use of a class method and static method.
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a
	# Person object by birth year
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a
	# Person is adult or not
	@staticmethod
	def isAdult(age):
		return age > 18

	def display(self):
		print("\nName and age are", self.name, self.age)


person1 = Person('John Hopkins', 21)
person2 = Person.fromBirthYear('John Hopkins', 1996)
person2.display()

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
