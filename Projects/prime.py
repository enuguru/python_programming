# generate prime numbers from 2 to 100 
# using nested for loops
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(2, 100):
    if is_prime(i):
        print(i, end=" ")   # print in one line
print()                     # print a newline
