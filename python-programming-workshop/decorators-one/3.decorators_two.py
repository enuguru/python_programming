
def my_decorator(some_function):

    def wrapper():
        num = 10
        if num == 10:
            print("Yes!")
        else:
            print("No!")
        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper


def just_some_function():
    print("reached here just_some_function!")


some_function_variable = my_decorator(just_some_function)
print(some_function_variable)
some_function_variable()
