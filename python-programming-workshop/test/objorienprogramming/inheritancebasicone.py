
class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
        print("This is base class")

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum
        print("This is derived class")

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

xobj = Person("Bob", "Simpson")
yobj = Employee("Homer", "Simpson", "1007")

print(xobj.Name())
print(yobj.GetEmployee())
