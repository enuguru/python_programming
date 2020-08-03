
def make_very_pretty(func):
    print("I got third decorated")
    return func

def make_more_pretty(func):
    print("I got second decorated")
    return func

def make_pretty(func):
    print("I got first decorated")
    return func


def ordinary():
    print("I am ordinary")


#let's decorate this ordinary function
# calling decorator the conventional way
pretty = make_very_pretty(make_more_pretty(make_pretty(ordinary)))
pretty()
