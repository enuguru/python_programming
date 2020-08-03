

import time
from array import array

# Create an int array, and a list.
list = list(range(0, 50))
arr = array("i", list)

print(time.time())

# Version 1: loop over array.
for i in range(0, 1000000):
    sum=0
    for value in arr:
        sum=sum+value

print(time.time())

# Version 2: loop over list.
for i in range(0, 1000000):
    sum=0
    for value in list:
	sum=sum+value
print(time.time())
