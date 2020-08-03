
class CountDown(object):

    def __init__(self, start):
        self.counter = start + 1

    def __next__(self): # __next__ in Python 3
        self.counter -= 1
        if self.counter <= 0:
            raise StopIteration
        return self.counter

    def __iter__(self):
        print("__iter__ is called")
        return self


cd = CountDown(5)
print(cd)
for x in cd:
    print(x)
