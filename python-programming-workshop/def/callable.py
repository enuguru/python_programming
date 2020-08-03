

#Callable. This built-in is not often useful, but I include it for completeness. 
#We can tell if an object (like an integer or lambda) can be called with it.

#Python that uses callable

method = lambda n: n == 2

# A method is callable.
if callable(method):
    print(True)

number = 8

# An integer is not callable.
if not callable(number):
    print(False)
