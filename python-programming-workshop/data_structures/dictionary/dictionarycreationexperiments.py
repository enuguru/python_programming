
newdict = {1:2.9, "Karthik G":35, 45:23, 23.34:"Ram"}
print(newdict)

#for items in range(4):
#print(newdict[items])

for items in newdict:
    print(items)

it = iter(newdict)
print(next(it))
print(next(it))
print(next(it))

print(newdict[1])
#newdict.append(45:"Ravi")
print(newdict)

anotherdict = {23:34, 45.66: "Jayashree", 45:(34,"Jayashree")}
print(anotherdict)
#anotherdict.append({34:10})
print(anotherdict)

seconddict = {4:[45,56,78], 56:[23,43,10], "Gururaj":[31,23,45], 23:{24:1}}
print(seconddict)
print(seconddict[56])
