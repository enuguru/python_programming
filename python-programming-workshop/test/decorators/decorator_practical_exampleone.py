
def benchmark(func):

# A decorator that prints the time a function takes to execute

    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print("{0} {1}".format(func.__name__, time.clock()-t))
        return res
    return wrapper


def logging(func):

#   A decorator that logs the activity of the script.
#  (it actually just prints it, but it could be logging!)

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("{0} {1} {2}".format(func.__name__, args, kwargs))
        return res
    return wrapper

def counter(func):
 
#  """
#   A decorator that counts and prints the number of times a function 
#   has been executed
#   """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper

@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

#print(reverse_string("Able was I ere I saw Elba"))
val = (reverse_string("Able was I ere I saw Elba"))
print(val)
for i in val:
    print(i,end='')
print("\n")


#print(reverse_string("Hi was that you that I saw in Boston Mall today morning"))
#print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))
