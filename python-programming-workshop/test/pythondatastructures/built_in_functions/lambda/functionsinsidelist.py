

#In the example above, a list of three functions was built up by embedding 
#lambda expressions inside a list. A def won't work inside a list literal 
#like this because it is a statement, not an expression. 
#If we really want to use def for the same result, we need temporary function 
#names and definitions outside:

 
def f1(x): return x ** 2  # here f1, f2 and f3 are the function names

def f2(x): return x ** 3

def f3(x): return x ** 4

# Reference by name
L = [f1, f2, f3]
for f in L:
    print(f(3))

print(L[0](3))
