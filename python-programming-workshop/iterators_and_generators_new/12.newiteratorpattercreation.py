
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

#To use such a function, you iterate over it using a for loop or use it with some other
#function that consumes an iterable (e.g., sum(), list(), etc.). For example:
for n in frange(0, 9, 0.5):
   print(n)
