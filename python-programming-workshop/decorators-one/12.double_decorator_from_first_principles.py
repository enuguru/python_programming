
def second_decorator(func):
    def inner():
        print("I am the second decorater")
        func()
    return inner

def first_decorator(func):
    def inner():
        print("I am the first decorater")
        func()
    return inner

def function_one():
    print("I am function one and I got decorated")

#ordinary()

# mypretty = make_pretty(ordinary)
# mypretty()

# let's decorate this ordinary function
#pretty = make_more_pretty(make_pretty(ordinary))
funcvar = first_decorator(second_decorator(function_one))
funcvar()
