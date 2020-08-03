
## Take five names as input and sort them. ##

# Take five names as input, and sort the names in
# alphabetical order

namelist = []
for count in range(3):
    name = input(" Give a name : ")
    namelist.append(name)

print(namelist[0])
print(name)

print(" The names in the namelist are : ",namelist)

sortedlist = sorted(namelist)
print(" The names in the namelist after sorting are : ", sortedlist)
