
# this is calling the decorator before calling the function
# but here we not using the decorator syntax, we are doing it
# from first principles

def make_pretty(func):
    def inner():
        print("This is the decorator function I got decorated")
        func()
    return inner

def ordinary():
    print("This is the main function I am ordinary")

#ordinary()

# let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty()
