
# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes

# A user defined class to represent Complex numbers
class Complex:

	# Constructor
	def __init__(self, real, imag):
	    self.real = real
	    self.imag = imag

	# For call to repr(). Prints object's information
	def __repr__(self):
	    return 'Rational(%s, %s)' % (self.real, self.imag)

	# For call to str(). Prints readable form
	def __str__(self):
	    return '%s + i%s' % (self.real, self.imag)


# Driver program to test above
t = Complex(10, 20)

# Same as "print t"
print (str(t))
print (repr(t))
