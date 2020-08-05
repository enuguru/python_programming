
newtuple = (1,2.9,"Karthik G")
print(newtuple)

for items in range(len(newtuple)):
    print(newtuple[items])

for items in newtuple:
    print(items)

yourtuple = (([[23,34],['l',23]],'p'),(23,45)) #nested definition of data structures
#recursive definition of data structures
print(yourtuple)

it = iter(newtuple)
print(next(it))
print(next(it))
print(next(it))

print(newtuple[0])
print(yourtuple[0])
#newtuple.append(45)
print(newtuple)

dictionary = {45:56}
anothertuple = (23, 45.66, "Karthika",(34,"Karthika"),{34:"Karthik G"},dictionary)
print(anothertuple)
#anothertuple.append({34:10})
print(anothertuple)
#anothertuple[0] = 3

mylist = ["Abinaya","Jayashree"]
secondtuple = ([45,56,78],[23,43,10],[31,23,45],mylist)
print(secondtuple)
secondtuple[0][0] = 34
#secondtuple[0] = 34
#mylist = ["Guru","ravi"]
print(secondtuple)
#mylist[0] = "ravi"
print(secondtuple[0])
print(secondtuple[2][0])
#recursive defintion of data structures
