
# the code below shows a simple tuple - 1st part of excercise

from math import sqrt

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
print(line_length)

# the code below shows a simple named tuple - 2nd part of our excercise

from collections import namedtuple
Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

line_length = sqrt((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)
print(line_length)


# the code below shows a namedtuple but accessed as a tuple 
# so backward compatible
# this is part 3 of our excercise

Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# use index referencing
line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
 # use tuple unpacking
x1, y1 = pt1


#However, as with tuples, attributes in named tuples are immutable:
# this is part 4 of our excercise

Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)

#pt1.x = 2.0
#AttributeError: can't set attribute

#If you want to be able change the values, you need another type. 
#There is a handy recipe for #mutable recordtypes which allow you 
#to set new values to attributes.


# here we use a new data type called rcdtype where we can change the values
# and is used like a named tuple
# this is part 5 of our excercise

#from rcdtype import *
#Point = recordtype('Point', 'x y')
#pt1 = Point(1.0, 5.0)
#pt1 = Point(1.0, 5.0)
#pt1.x = 2.0
#print(pt1[0])
