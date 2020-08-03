
import random

def m():
    # Get random number.
    n = random.randint(0, 3)
    print(n)
    # Return true if number is less than 3.
    return n <= 2

# Call method until it returns false.
while m():
    # Do nothing in the loop.
    pass
