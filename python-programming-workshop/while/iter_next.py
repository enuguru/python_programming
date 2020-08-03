

#Iter, next method. With iter we get an iterator variable. We must call next() on 
#this iterator to use it. Here I call next() to get successive values from a 
#list—no loop is needed.


values = [1, 10, 100, 1000]
i = iter(values)

# Call the next built-in on an iter.
# ... This style of code is not often useful.
value = next(i)
print(value)

value = next(i)
print(value)

value = next(i)
print(value)

value = next(i)
print(value)

