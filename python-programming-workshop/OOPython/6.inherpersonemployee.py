
# this program demonstrates how the derived class and 
# the base class work with each other and the syntax
# for inheritance in python

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

xobj = Person("Marge", "Simpson")
yobj = Employee("Homer", "Simpson", "1007")

print(xobj.Name())
print(yobj.Name())
print(yobj.GetEmployee())
