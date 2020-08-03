
def apply(f, n):
    print(f(n))

# Create two lambdas.
square = lambda n: n * n
cube = lambda n: n * n * n

print(square(3))
# Pass lambdas to apply method.
apply(square, 4)
apply(cube, 3)
