
mylist = []
mylist.append(2)
mylist.append(2)
print(mylist)

newlist = list([34,45])
print(newlist)

mylist.append(34)
mylist.append(67)
mylist.append(56)
mylist.append(77)

print(mylist.index(67))
print(mylist.index(77))

if 67 in mylist:
    print("present")
else:
    print("not present")

del(mylist[2])
print(mylist)
