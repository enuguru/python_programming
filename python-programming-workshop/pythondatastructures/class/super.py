

#Super. With the super() built-in, we can get the parent of a class. 
#This gets the immediate ancestor. Here we call super() within the 
#Circle class, which references its parent class, Shape.

#Print:The name method from Circle prints "Circle." Then name() from 
#Shape is also called.

#Python that uses super

class Shape:
    def name(self):
        print("Shape")

class Circle(Shape):
    def name(self):
        print("Circle")
        # Call name method from parent class.
        super().name()

# Create Circle and call name.
c = Circle()
c.name()
