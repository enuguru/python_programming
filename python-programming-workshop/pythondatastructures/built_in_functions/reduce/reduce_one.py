
#The reduce is in the functools in Python 3.0. It is more complex. 
#It accepts an iterator to process, but it's not an iterator itself. It 
#returns a single result:
#At each step, reduce passes the current product or division, along with the next 
#item from 
#the list, to the passed-in lambda function. By default, the first item in the sequence 
#initialized the starting value.

from functools import reduce
print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))
print(reduce((lambda x, y: x / y), [1, 2, 3, 4]))
