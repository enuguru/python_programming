

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
