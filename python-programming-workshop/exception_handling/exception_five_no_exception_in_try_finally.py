

#finally block is always executed after leaving the try statement. 
#In case if some exception was not handled by except block, 
#it is re-raised after execution of finally blocka

#finally block is used to deallocate the system resources.
#One can use finally just after try without using except block, 
#but no exception is handled in that case

# Python program to demonstrate finally
  
# No exception Exception raised in try block

try:
    num = 5//0 # raises divide by zero exception.
    print(num)
  
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
      
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')  
