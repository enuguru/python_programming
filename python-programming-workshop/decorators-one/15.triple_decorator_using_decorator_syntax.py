
def make_very_pretty(func):
    print("make_very_pretty I got third decorated")
    print("Doing something in the third")
    return func

def make_more_pretty(func):
    print("make_more_pretty I got second decorated")
    print("Doing something in the second")
    return func

def make_pretty(func):
    print("make_pretty I got first decorated")
    print("Doing something in the first")
    return func

@make_very_pretty
@make_more_pretty
@make_pretty
def ordinary():
    print("I am the actual function I am ordinary")

ordinary()
