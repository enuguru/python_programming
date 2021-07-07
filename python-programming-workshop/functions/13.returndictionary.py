
#!/usr/bin/python

# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   insidevar = arg1 + arg2
   yourdict = {23:45,45:"Python",77:"awesome"}
   print("I am inside the function : ", insidevar)
   return yourdict;

# Now you can call sum function
outsidevar = sum( 10, 20 )
print("I am ouside the function :", outsidevar) 
