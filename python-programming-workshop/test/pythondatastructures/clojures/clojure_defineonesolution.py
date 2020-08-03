
def anotherfunc(h):
    h = h + 5
    def func():
        return h
    return func

print(anotherfunc(12)())

val = anotherfunc(12)
print(val)
print(val())
