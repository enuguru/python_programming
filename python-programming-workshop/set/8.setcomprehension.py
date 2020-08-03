
#set comprehensions and list comprehensions are basically the same, 
#but the former returns a set instead of a list:

setone = {x for x in [1, 1, 2, 3, 3, 1]}
print(setone)

#It's the same as:
#in the below code we specifically use the set function to create a set
settwo = set([i for i in [1, 1, 2, 3, 3, 1]])
print(settwo)
