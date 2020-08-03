def decorate(f):
    def wrapped_function():
        print("Function is being called")
        f()
        print("Function call is finished")
    return wrapped_function

@decorate
def my_function():
    print("Hello world")

my_function()
