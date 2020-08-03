
#Ljust, rjust. These pad strings. They accept one or two arguments. The first argument 
#is the total length of the result string. The second is the padding character.

#Tip: If you specify a number that is too small, ljust and rjust do nothing. 
#They return the original string.

#Python that uses ljust, rjust

s = "Paris"

# Justify to left, add periods.
print(s.ljust(10, ";"))

# Justify to right.
print(s.rjust(10))
