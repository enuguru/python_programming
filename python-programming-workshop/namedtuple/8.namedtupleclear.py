
# this is using a normal tuple
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
print(line_length)

# now I am using a namedtuple called Point
# see the code has become more readable now

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

from math import sqrt
line_length = sqrt((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)
print(line_length)


#However, named tuples are still backwards compatible with normal tuples, 
#so the following will still work:

Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

from math import sqrt
# use index referencing
line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
print(line_length)
# use tuple unpacking
x1, y1 = pt1
print(x1, y1)

# you can even use namedtuple as base classes
class Point(namedtuple('Point', 'x y')):
    [...]
