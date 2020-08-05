
# Python program to demonstrate finally
  
try:
    k = 5//2 # No exception raised
    print(k)
  
# intends to handle zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
      
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed') 
