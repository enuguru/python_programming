
# relationship between base and derived class
# use of the word super

# This __str__ method is called when print() or str() function is invoked on an object. 
# This method must return the String object. If we don't implement __str__() function 
# for a class, then built-in object implementation is used that actually calls __repr__() function
# here we are using the builtin __repr__ function - you can see it is not very useful

class Person:

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)

class Employee(Person):

    def __init__(self, first, last, age, staffnum):
        super().__init__(first, last, age)
        self.staffnumber = staffnum

    def __str__(self):
        return super().__str__() + ", " +  self.staffnumber

xobj = Person("Marge", "Simpson", 36)
yobj = Employee("Homer", "Simpson", 28, "1007")

m = xobj.__repr__()
print(m)
n = yobj.__repr__()
print(n)
