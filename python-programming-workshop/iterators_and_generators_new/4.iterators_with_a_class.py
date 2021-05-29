
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max
        print(self.max)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(7)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
input("Press Enter to continue...")

print(next(i))

input("Press Enter to continue...")
print(next(i))
input("Press Enter to continue...")
print(next(i))
input("Press Enter to continue...")
print(next(i))
input("Press Enter to continue...")
print(next(i))
input("Press Enter to continue...")
print(next(i))
input("Press Enter to continue...")
print(next(i))
input("Press Enter to continue...")
print(next(i))
input("Press Enter to continue...")
print(next(i))
input("Press Enter to continue...")
