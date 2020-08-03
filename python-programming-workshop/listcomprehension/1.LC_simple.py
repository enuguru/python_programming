
import math

# using normal method
y = [1,2,3,4,5,6,7,8,9,10]
print(y)

# using list comprehension method
x = [i for i in range(1,11)]
print(x)


q = [i*10 for i in range(1,11)]
print(q)

p = [i*i for i in range(1,11)]
print(p)

p = [i**2 for i in range(1,11)]
print(p)

s = [i*i*i for i in range(1,11)]
print(s)

r = [int(math.sqrt(i)) for i in p]
print(r)


