

#Python program that uses isinstance

class A:
    def welcome(self):
        # Not called.
        print("Welcome")

# This is an instance of A.
a = A()

if isinstance(a, A):
    print(1)

# This is an instance of the list class.
b = [1, 2, 3]

if isinstance(b, A):
    # Not reached.
    print(2)

if isinstance(b, list):
    print(3)
