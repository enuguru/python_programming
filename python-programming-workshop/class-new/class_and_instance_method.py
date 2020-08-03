


#Classmethod. This is a function decorator. We apply it by specifying 
#@classmethod before "def." It is a combination of an instance, and static, 
#method. It can be called either way.

#So: We can call the classmethod example, with the syntax Box.
#example or on a Box instance "b."

#Class: The class argument ("cls" here) can be used as to create a type 
#and return it. Or we can ignore it.

#Python that uses classmethod

class Box:
    @classmethod
    def example(cls, code):
        # This method can be used as an instance or static method.
        print("Method called:", code)

# Use classmethod as a static method.
Box.example("cat")

# Use classmethod as an instance method.
b = Box()
b.example("dog")
