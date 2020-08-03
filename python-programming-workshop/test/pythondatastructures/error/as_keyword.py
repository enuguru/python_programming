
#As-keyword. We can name a variable within an except statement. We use the 
#as-keyword for this. Here we name the IOError "err" and can use it within the clause.

#Python program that uses as, except

try:
    f = open("does-not-exist")
except IOError as err:
    # We can use IOError as an instance.
    print("Error:", err)
    print("Number:", err.errno)
