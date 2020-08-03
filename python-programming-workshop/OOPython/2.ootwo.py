
# what is the class here?  - Point
# what is the object here? - p1, p2

# what are the variables here? x,y

# what is . dot notation? p1.x ? - x variable belonging to 
#                                  p1 class
#                         p2.y ? - y variable belonging to 
#                                  p2 class

class Point:
    pass

p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

print(p1.x, p1.y)
print(p2.x, p2.y)
