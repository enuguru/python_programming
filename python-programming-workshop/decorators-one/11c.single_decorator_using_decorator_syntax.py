
# here we are using the decorator syntax and doing
# the same thing done in the previous program
# does'nt this look cleaner ?

def decorator_function(func):
    print("I am the decorator function and I am doing decoration job")
    func()

@decorator_function
def function_one():
    print("I am function_one, I got decorated")

function_one()

#syntactic sugar
