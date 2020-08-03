class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        print("Hi I am now in __repr__ function")
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        print("Hi I am now in __str function")
        return '({0.x}, {0.y})'.format(self)

c = Pair(10,23)
print(Pair(23,34).__repr__())
print(c)

