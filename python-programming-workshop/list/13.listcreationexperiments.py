
newlist = [1,2.9,"Karthik G"]
print(newlist)

for items in range(len(newlist)):
    print(newlist[items])

for items in newlist:
    print(items)

it = iter(newlist)
print(next(it)) 
print(next(it))
print(next(it))

print(newlist[0])
newlist.append(45)
print(newlist)

anotherlist = [23, 45.66, "Jayashree",(34,"Jayashree")]
print(anotherlist)
#anotherlist.append({34:10}) // associative array
print(anotherlist)

secondlist = [[45,56,78],[23,43,10],[31,23,45]]
print(secondlist)
print(secondlist[0][2])

thirdlist = [[[45,56,78],[23,43,10],[31,23,45]],(([1,2],"Jayashree",[4,24]),34)]
print(thirdlist)
