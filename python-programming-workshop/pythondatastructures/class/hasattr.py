

#Hasattr

#There are two built-in functions other than getattr and setattr. With hasattr we 
#see if an attribute (field) exists on the class instance. It returns True or False. 
#With delattr we remove an attribute from the class.

#Del: Delattr is another syntax form for the del operator. We use this operator to 
#remove things (as from a dictionary).

#Python program that uses hasattr, delattr

class Box:
    pass

box = Box()

# Create a width attribute.
setattr(box, "width", 15)

# The attribute exists.
if hasattr(box, "width"):
    print(True)

# Delete the width attribute.
delattr(box, "width")

# Width no longer exists.
if not hasattr(box, "width"):
    print(False)
