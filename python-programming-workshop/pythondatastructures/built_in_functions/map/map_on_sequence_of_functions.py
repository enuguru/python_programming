
#map is described as follows - map(aFunction, aSequence)

#While we still use lamda as a aFunction, we can have a list of functions as aSequence:
#this is a very special way of doing map, here we apply a function on a sequence of functions
#interesting ....

def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]
for r in range(5):
    value = list(map(lambda x: x(r), funcs))
    print(value)
