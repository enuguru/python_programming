
# nice solution karthick, neat and clean
# any other solutions you can think of
# a clue is it involves counting characters

strone = "apple"
strtwo = "orange"
strthree = "cinema"
strfour = "iceman"

listone = list(strone)
listtwo = list(strtwo)
listthree = list(strthree)
listfour = list(strfour)

listone.sort()
listtwo.sort()
listthree.sort()
listfour.sort()

print(listone)
print(listtwo)
print(listthree)
print(listfour)

if listone == listtwo:
    print(strone + " and " + strtwo + " are anagrams")
else:
    print(strone + " and " + strtwo + " are not anagrams")

if listthree == listfour:
    print(strthree + " and " + strfour + " are anagrams")
else:
    print(strthree + " and " + strfour + " are not anagrams")
