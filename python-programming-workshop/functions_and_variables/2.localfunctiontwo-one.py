
a = 90
def outer():
    a = 325
    def inner():
        a = 0
        a = a + 10
        def innerinner():
            x = 80
            print(x)
        print(a)
        innerinner()
        a = a + 20
        print(a)
    print(a)
    inner()

print(a)
outer()
