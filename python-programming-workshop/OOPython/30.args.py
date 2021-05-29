
def multiply(*args):
    z = 1
    for num in args:
        z = z + num
    print(z)
    print(args)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)
multiply(3, 5, 10, 6, 10)
