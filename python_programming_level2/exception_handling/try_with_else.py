# Program to depict else clause with try-except
# Function which returns a/b
def one(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result is 0")
	else:
		print (c)

#one(2.0, 3.0)
one(3.0, 3.0)
