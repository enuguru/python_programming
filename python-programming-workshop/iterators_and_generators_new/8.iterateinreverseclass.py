
class Countdown:
    def __init__(self, start):
        self.start = start
    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

# Reverse iterator
def __reversed__(self):
    n = 1
    while n <= self.start:
       	yield n
        n += 1

c=Countdown(9)
print(c)
a=iter(c)
print(next(a))
