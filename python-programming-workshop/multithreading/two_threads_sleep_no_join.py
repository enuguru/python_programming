
# Python program to illustrate the concept
# of threading
# importing the threading module

import threading
import time

def print_cube(num):

    print("Thread two starts")
    print("Cube: {}".format(num * num * num))
    print("thread two starts sleeping")
    time.sleep(5)
    print("Thread two completes")


def print_square(num):

    print("Thread one starts")
    print("Square: {}".format(num * num))
    print("thread one starts sleeping")
    time.sleep(5)
    print("Thread one completes")


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

for count in range(1000):
        print(count,end=" ")
# both threads completely executed
print("Done!")

