
#Id method. Every object has an id. This is unique to the instance. 
#Its exact number is an implementation detail and will vary between 
#program executions. Here we look at class ids.

#Note: Ids may be reused when objects are removed by the garbage collector 
#and are not in use. They are rarely useful in code.

#Python that uses id

class Cat:
    def __init__(self, color):
        self.color = color

cat1 = Cat("black")
cat2 = Cat("orange")

# Each object has a unique id.
# ... The ids may vary between runs.
print(id(cat1))
print(id(cat2))
