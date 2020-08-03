

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

# this prints the function reference or address of the function
print(fib)

f = fib
# this also prints the function reference or address of the function
print(f)
# this calss the function through reference or address of the function
# this looks like a function pointer in C
f(100)
