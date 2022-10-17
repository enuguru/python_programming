
def second_decorator(func):
    print("I am the second decorator function")
    return func

def first_decorator(func):
    print("I am the first decorator function")
    return func

@second_decorator
@first_decorator
def function_one():
    print("I am function one and I got decorated")

function_one()
