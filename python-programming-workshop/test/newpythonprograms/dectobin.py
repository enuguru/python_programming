

# Python program to convert decimal number into binary number using recursive function

def binary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       binary(n//2)
   print(n % 2,end = '')

# Take decimal number from user
dec = int(input("Enter an integer: "))
binary(dec)
