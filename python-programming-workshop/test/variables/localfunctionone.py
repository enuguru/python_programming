
def outer():
    a = 325
    def inner():
        print(a)
    inner()
outer()
