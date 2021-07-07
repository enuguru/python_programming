
#!/usr/bin/python

# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   insidevar = arg1 + arg2
   yourtuple = (23,45,77)
   print("I am inside the function : ", insidevar)
   return yourtuple;

# Now you can call sum function
outsidevar = sum( 10, 20 )
print("I am ouside the function :", outsidevar) 
