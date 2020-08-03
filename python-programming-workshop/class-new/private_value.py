
#constructor
#destructor
#copy constructor
#copy assignement operator

# Python program that uses two-underscore variable
# two-underscore variable is used as private variable but can accesses
# outside the class with _A_value

class A:
    # Init.
    def __init__(self, value): # __init__  constructor dunder methods
        self.__value = value
        print("Now Iam entering the constructor")

    # Two-underscore name.
    __value = 0

# Create the class.
a = A(5)

# [1] Cannot use two-underscore name.
# print(a.__value)

# [2] Must use mangled name.
print(a._A__value)
