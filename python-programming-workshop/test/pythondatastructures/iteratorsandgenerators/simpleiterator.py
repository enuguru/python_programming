
#create a simple iterator

items = [41, 772, 333]
# Get the iterator
it = iter(items) # Invokes items.__iter__()
print(it)
# Run the iterator
print(next(it)) # Invokes it.__next__()
print(next(it))
print(next(it))
