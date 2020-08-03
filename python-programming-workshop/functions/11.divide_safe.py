
#A method. We use def for "dividesafe." This method receives two arguments. And in its body, 
#it checks the argument "b" against zero. It returns -1 if the division would cause an error.

#However:The method returns the result of the division expression in every other case.

#Note: This method receives arguments and returns explicit values. It is possible for a 
#def-method in Python to return no value.

#Based on: Python 3

#Python program that uses def

def dividesafe(a, b):
    # Handle zero denominator.
    if b == 0:
        return -1
    # Divide.
    return a / b

# Use method.
print(dividesafe(10, 5))
print(dividesafe(10, 0))
