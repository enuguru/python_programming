


#Issubclass. This determines if one class is derived from another. With this 
#built-in method, we pass two class names (not instances).

#Return:If the first class inherits from the second, issubclass returns true. 
#Otherwise it returns false.

#Tip:This is rarely useful to know: a class is considered a subclass of itself. 
#The third issubclass call below shows this.

class A:
    def hello(self):
        print("A says hello")

class B(A):
    def hello(self):
        print("B says hello")

# Use the derived class.
b = B()
b.hello()

# See if B inherits from A.
if issubclass(B, A):
    print(1)

# See if A inherits from B.
if issubclass(A, B):
    # Not reached.
    print(2)

# See if A inherits from itself.
if issubclass(A, A):
    print(3)
