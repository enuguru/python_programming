
# Python program to illustrate the concept
# of threading
# importing the threading module

import threading

def print_cube(num):

	print("Cube: {}".format(num * num * num))
	for count in range(201):
		print(count,end= " ")

def print_square(num):

	print("Square: {}".format(num * num))
	for count in range(301):
		print(count,end=" ")


t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
#t1.join()
# wait until thread 2 is completely executed
#t2.join()

for count in range(101):
        print(count,end=" ")
# both threads completely executed
print("Done!")
