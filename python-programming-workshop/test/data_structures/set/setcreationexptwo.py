
# initialize a with {}
a = {}

# check data type of a
print(type(a))

# initialize a with set()
a = set()

# check data type of a
print(type(a))

# Output: {1, 2, 3, 4}
my_set = {1,2,3,4,3,2}
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# If you uncomment line #12,
# this will cause an error.
# TypeError: unhashable type: 'list'

#your_set = {1, 2, [3, 4]}

# we can make set from a list
# Output: {1, 2, 3}
# the below one is different, here we are making a set 
# from a list
my_set = set([1,2,3,2])
print(my_set)
