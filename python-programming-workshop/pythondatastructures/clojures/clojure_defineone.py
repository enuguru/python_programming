
def func(): 
    return h

def anotherfunc(h):
    return func

print(anotherfunc(12)())
