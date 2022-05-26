# Python program to
# demonstrate __new__

# don't forget the object specified as base
class A(object):
	def __new__(cls):
		print("Creating instance")
		return super(A, cls).__new__(cls)

	def __init__(self):
		print("Init is called")

A()
