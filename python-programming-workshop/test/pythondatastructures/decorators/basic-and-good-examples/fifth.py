
def make_more_pretty(func):
    print("I got second decorated")
    return func

def make_pretty(func):
    print("I got first decorated")
    return func


@make_more_pretty
@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()

