
#namedtuple is a factory function for making a tuple class. With that class 
#we can create tuples that are callable by name also.

import collections

#Create a namedtuple class with names "a" "b" "c"
Row = collections.namedtuple("Row", ["a", "b", "c"], verbose=False, rename=False)   

row = Row(a=1,b=2,c=3) #Make a namedtuple from the Row class we created

print row    #Prints: Row(a=1, b=2, c=3)
print row.a  #Prints: 1
print row[0] #Prints: 1

row = Row._make([2, 3, 4]) #Make a namedtuple from a list of values

print row   #Prints: Row(a=2, b=3, c=4)
