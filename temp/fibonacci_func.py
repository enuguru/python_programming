
# fibonacci_func.py

def fibonacci_of(n):
    # Validate the value of n
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(
            f'Positive integer number expected, got "{n}"'
        )

    # Handle the base cases
    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, 
        # remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


print(fibonacci_of(10))
