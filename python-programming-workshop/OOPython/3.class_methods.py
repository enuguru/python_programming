
class Point:
    def reset(self):
        self.x = 0
        self.y = 0


p1 = Point() # an object p1 is created or instantiated
p1.reset()   # a function called "reset" in "point" class is 
             # called
print(p1.x, p1.y)

p2 = Point()
p2.reset()
print(p2.x,p2.y)
