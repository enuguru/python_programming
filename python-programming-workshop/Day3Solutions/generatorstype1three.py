
class Squares(object):
    
    def __init__(self, start, stop):
       self.start = start
       self.stop = stop

    def __iter__(self): 
        return self

    def current(self):
       return self.start

    def next(self):
       if self.start >= self.stop:
           raise StopIteration
       current = self.start * self.start
       self.start += 1
       return current

a = 2
b = 7
iterator = Squares(a, b)
for i in iterator:
    print(i)
print(iterator.current())
