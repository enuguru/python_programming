
# this is calling the decorator before calling the function
# but here we not using the decorator syntax, we are doing it
# from first principles

def decorator_function(func):
    def inner():
        print("I am the decorator function and I am doing decoration job")
        func()
        print("after decoration")
    return inner

def function_one():
    print("I am function_one and I got decorated")


# let's decorate function_one
funcvar = decorator_function(function_one) #higher order functions
funcvar()
