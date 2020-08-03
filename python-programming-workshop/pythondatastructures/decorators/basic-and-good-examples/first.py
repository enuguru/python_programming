
# this is calling the decorator before calling the function

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

#ordinary()

# let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty()
