

#Hash. When comparing objects, a hash code can be used for more speed. 
#A dictionary uses hashes. With __hash__ we implement custom hash computations. 
#A unique value is a good hash.

#Here: In this program two Snake objects, with the same names and colors, 
#are created. The unique_id is used to compute the hash.

#Python that uses hash on class

class Snake:
    def __init__(self, name, color, unique_id):
        self.name = name
        self.color = color
        self.unique_id = unique_id
    def __hash__(self):
        # Hash on a unique value of the class.
        return int(self.unique_id)

# Hash now is equal to the unique ID values used.
p = Snake("Python", "green", 55)
print(hash(p))

p = Snake("Python", "green", 105)
print(hash(p))
