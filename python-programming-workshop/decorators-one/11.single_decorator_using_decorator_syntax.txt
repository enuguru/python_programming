
# here we are using the decorator syntax
# and doing the same thing done in problem 1
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()
