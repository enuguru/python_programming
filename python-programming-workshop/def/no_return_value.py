

#No return value. Methods in Python do not have to return a value. If we use the "return" 
#statement alone, no value is returned. This is called a void method in other languages.

#Method that returns no value: Python

def printname(first, middle, last):
    # Validate middle initial length.
    if len(middle) != 1:
        print("Middle initial too long")
        return
    # Display.
    print(first + " " + middle + ". " + last)

# Call method.
printname("Jake", "R", "Chambers")
printname("Jake", "", "Chambers")
