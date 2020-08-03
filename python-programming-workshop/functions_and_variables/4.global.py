
x = 4
def outer():
    x = 1
    def inner():
        global x
        #x = 4
        print("this is a global variable x printed from inner function:", x)

    inner()
    print("this is the value of x in outer function:", x)

outer()
print("this is the global variable x printed from outside everything:", x)
