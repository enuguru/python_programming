
#function return
def transform(n):
    return lambda x: x + n

f = transform(0)
print(f(4))
