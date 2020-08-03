

# tuple with different data types and with different printing styles ##

# write a program to create a tuple with different data
# types and do the following

# a) delete an element tuple -- not possible
# b) add an element to the tuple  -- not possible
# c) print the element which is 2nd from the beginning
# d) print the element which is 2nd from the last

newtuple = (5,'f',"fantastic",2.345)
print(" The elements in the tuple are : ",newtuple)

print(" The second element of the tuple is : ", newtuple[1])
print(" The elements (from second to last) in the tuple are : ",newtuple[1:])
print(" The last element of the tuple is : ",newtuple[-1])
print(" The elements in the tuple after reversing(from last till second) : ",newtuple[-1:0:-1])
print(" All the elements in the tuple after reversing are : ",newtuple[-1::-1])

newstring = "fantastic"
print(" The reverse of the string ' fantastic ' is : ",newstring[-1::-1])
