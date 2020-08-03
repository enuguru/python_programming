

oldlist = [23,45,45,67,89,71,23,34,45]

newlist = []

for val in oldlist:
    if val not in newlist:
        newlist.append(val)
print(newlist)


newdictionary = {}

for val in oldlist:
    newdictionary[val] =0

for key,value in newdictionary:
    print(key,end=" ")
    print(value,end=" ")
print()


# {23:0,45:0,67:0,89:0,71:0,34:0}
