
# This is called binding the variable 
# as an argument to the local function a=a

def outer():
    a = 325
    def inner(a=a):
        a += 10
        print(a)
    inner()
outer()
