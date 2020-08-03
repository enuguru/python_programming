

#Finally. This clause is always executed, even if an error is raised. We can 
#use "finally" statements as a way to clean up, or ensure completion of tasks.

#Python program that uses finally

try:
    # An error occurs.
    x = 1 / 0
except:
    # Except clause:
    print("Error encountered")
finally:
    # Finally clause:
    print("Finally clause reached")
