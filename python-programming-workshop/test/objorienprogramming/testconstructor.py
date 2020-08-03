
class Person:

    def __init__(self, first, last):
        print("This is base class")


class Employee(Person):

    def __init__(self, first, last):
        print("This is derived class")
        Person.__init__(self,first,last)

yobj = Employee("Homer", "Simpson")

#print(xobj.Name())
#print(yobj.GetEmployee())
