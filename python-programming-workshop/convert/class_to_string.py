

#Python that converts class to string

class Test:
    def __init__(self):
        self.size = 1
        self.name = "Python"

    def __repr__(self):
        # Return a string.
        return "Size = " + str(self.size) + ", Name = " + str(self.name)

t = Test()

# Str and repr will both call into __repr__.
s = str(t)
r = repr(t)

# Display results.
print(s)
print(r)
