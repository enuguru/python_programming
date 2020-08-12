
# Python 3 implementation of above approach

# Function to convert decimal to
# binary number
def bin(n):
    if (n > 1):
        bin(n >> 1)
    print(n&1,end=" ")

# Driver code
bin(131)
print()
bin(3)

