
# Program to define the use of super()
# function in multiple inheritance
class GFG1:
	def __init__(self):
		print('HEY !!!!!! GfG I am initialised(Class GEG1)')

	def sub_GFG(self, b):
		print('Printing from class GFG1:', b)

# class GFG2 inherits the GFG1
class GFG2(GFG1):
	def __init__(self):
		print('HEY !!!!!! GfG I am initialised(Class GEG2)')
		super().__init__()

	def sub_GFG(self, b):
		print('Printing from class GFG2:', b)
		super().sub_GFG(b + 1)

# class GFG3 inherits the GFG1 ang GFG2 both
class GFG3(GFG2):
	def __init__(self):
		print('HEY !!!!!! GfG I am initialised(Class GEG3)')
		super().__init__()

	def sub_GFG(self, b):
		print('Printing from class GFG3:', b)
		super().sub_GFG(b + 1)


# main function
if __name__ == '__main__':

	# created the object gfg
	gfg = GFG3()

	# calling the function sub_GFG3() from class GHG3
	# which inherits both GFG1 and GFG2 classes
	gfg.sub_GFG(10)

