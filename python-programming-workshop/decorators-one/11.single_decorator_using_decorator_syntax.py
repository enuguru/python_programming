
# here we are using the decorator syntax and doing
# the same thing done in the previous program
# does'nt this look cleaner ?

def new_name_function(func):

    def inner():
        print("I am the decorator_function, and I am doing decoration job")
        func()
        print("This line is printed after the function_one() call")
        return "Coming bcck to original call"

    return inner


@new_name_function
def function_one():
    print("I am function_one, I got decorated")

print(function_one())

#syntactic sugar
