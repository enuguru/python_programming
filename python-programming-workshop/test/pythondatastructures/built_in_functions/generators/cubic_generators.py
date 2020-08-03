
def cubic_generator(n):
	for i in range(n):
		yield i ** 3

for i in cubic_generator(5):
	print(i,  end=' : ')  # Python 3.0
        #print i,             # Python 2.x
