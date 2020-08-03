

def make_more_pretty(func):
    def inner():
        print("I got second decorated")
        func()
    return inner

def make_pretty(func):
    def inner():
        print("I got first decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")


#ordinary()

# mypretty = make_pretty(ordinary)
# mypretty()

# let's decorate this ordinary function
pretty = make_more_pretty(make_pretty(ordinary))
pretty()
