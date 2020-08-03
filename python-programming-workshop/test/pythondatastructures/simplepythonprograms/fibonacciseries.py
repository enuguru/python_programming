

# This program calculates the Fibonacci sequence
a = 0
b = 1
count = 0
max_count = 20
 
while count < max_count:
    count = count + 1
    print(a, end=" ")  # Notice the magic end=" " in the print function arguments  
                       # that keeps it from creating a new line.
    old_a = a    # we need to keep track of 'a' since we change it.
    a = b
    b = old_a + b
print()  # gets a new (empty) line.
