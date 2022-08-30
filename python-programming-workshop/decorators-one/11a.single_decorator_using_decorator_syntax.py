
# here we are using the decorator syntax and doing
# the same thing done in the previous program
# does'nt this look cleaner ?

def decorator_function(func):

    def inner():
        print("I am the decorator_function, I am doing the decoration job")
        func()

    return inner


@decorator_function
def function_one():
    print("I am function_one, I got decorated")

function_one()

#syntactic sugar
