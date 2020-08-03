

#Staticmethod. A static method accepts no self instance. Most methods in a 
#class accept a first argument with name "self." With the @staticmethod 
#decorator, though, we omit this argument.

#Tip: Static methods can return any value. They can accept any arguments. 
#They are called with the class name, or on an instance.

#Also: It makes no difference whether you call a static method with Box.Message 
#or on an instance like b.Message.

#Python that uses staticmethod

class Box:
    @staticmethod
    def Message(a):
        print("Box Message", a)

# Call static method with type.
Box.Message(1)

# Call static method with instance.
b = Box()
b.Message(2)
