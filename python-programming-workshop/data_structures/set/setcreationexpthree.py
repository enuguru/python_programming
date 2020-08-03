
#How to change a set in Python?

#Sets are mutable. But since they are unordered, indexing have no meaning.

#We cannot access or change an element of set using indexing or slicing. 
#Set does not support it.

#We can add single element using the add() method and multiple elements using the 
#update() method. The update() method can take tuples, lists, strings or other sets 
#as its argument. In all cases, duplicates are avoided.

# initialize my_set
my_set = {1,3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

#my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)
