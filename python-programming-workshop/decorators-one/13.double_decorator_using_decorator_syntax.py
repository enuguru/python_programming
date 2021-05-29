
def make_more_pretty(func):
    print("make_more_pretty I got second decorated")
    return func

def make_pretty(func):
    print("make_pretty I got first decorated")
    return func


@make_more_pretty
@make_pretty
def ordinary():
    print("I am the actual function to be called I am ordinary")

ordinary()
