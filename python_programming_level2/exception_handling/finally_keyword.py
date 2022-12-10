
# Python program to demonstrate finally
# No exception Exception raised in try block
try:
	k = 5//0 # raises divide by zero exception.
	print(k)

except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	print('This is always executed')
