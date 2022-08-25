
# Python program to understand the classmethod

class StudentName:

	# create a variable
	name = "Rishabh Saini"

	# create a function
	def print_name(obj):
		print("The name is : ", obj.name)

obj = StudentName();
obj.name = "yourname"
obj.print_name()
#StudentName.print_name()

# create print_name classmethod
# before creating this line print_name()
# It can be called only with object not with class
StudentName.print_name = classmethod(StudentName.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
StudentName.print_name()
