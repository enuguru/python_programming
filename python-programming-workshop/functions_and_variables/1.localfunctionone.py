
a = 67

def outer():
    a = 325
    def inner():
        a = 10
        print(a)
    inner()
    print(a)

def venkatesh():
    a = 90
    print(a)

print(a)
outer()
venkatesh()
