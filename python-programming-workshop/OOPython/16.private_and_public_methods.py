
# Python program to
# demonstrate private methods
  
# Creating a Base class
class Base:
 
    _myvar = 10
    # Declaring public method
    def fun(self):
        print("Public method")
  
    # Declaring private method
    def __fun(self):
        print("Private method")
  
# Creating a derived class

class Derived(Base):
    def __init__(self):
          
        # Calling constructor of
        # Base class
        Base.__init__(self)
          
    def call_public(self):
          
        # Calling public method of base class
        print("\nInside derived class")
        self.fun()
          
    def call_private(self):
        print(self._myvar)  
        # Calling private method of base class
        self.__fun()
  
# Driver code
obj1 = Base()
  
# Calling public method
obj1.fun()
  
obj2 = Derived()
obj2.call_public()
obj2.call_private()
  
# Uncommenting obj1.__fun() will
# raise an AttributeError
  
# Uncommenting obj2.call_private()
# will also raise an AttributeError
