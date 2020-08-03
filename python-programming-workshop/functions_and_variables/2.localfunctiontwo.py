
a = 90
def outer():
    a = 325
    def inner():
        a = 0
        a = a + 10
        print(a)
        a = a + 20
        print(a)
    print(a)
    inner()

print(a)
outer()
