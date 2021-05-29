
def badri(some_function):
    print("This is the decorator called before actual function call")
    return some_function

@badri
def just_some_function():
    print("This is the actual function which you wanted to run!")

just_some_function()
