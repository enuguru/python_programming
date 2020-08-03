
#create a simple iterator

items = [1, 2, 3]
# Get the iterator
it = iter(items) # Invokes items.__iter__()
# Run the iterator
print(next(it)) # Invokes it.__next__()
print(next(it))
print(next(it))
