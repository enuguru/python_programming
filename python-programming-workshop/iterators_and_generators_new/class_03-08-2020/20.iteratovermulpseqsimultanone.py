
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a,b):
    print(i)
print("--------------------------------------")

from itertools import zip_longest
for i in zip_longest(a,b):
    print(i)

print("--------------------------------------")

for i in zip_longest(a, b, fillvalue=0):
    print(i)

print("--------------------------------------")

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]


#Using zip(), you can pair the values together to make a dictionary like this:
#s = dict(zip(headers,values))

#Alternatively, if you are trying to produce output, you can write code like this:
#for name, val in zip(headers, values):
for name, val in zip(headers, values):
    print(name, '=', val)

print("--------------------------------------")

#It’s less common, but zip() can be passed more than two sequences as input. For this
#case, the resulting tuples have the same number of items in them as the number of input
#sequences. For example:

a = [1, 2, 3]
b = [10, 11, 12]
c = ['x','y','z']
for i in zip(a, b, c):
    print(i)

print("--------------------------------------")

print(zip(a, b))
print(list(zip(a, b)))
