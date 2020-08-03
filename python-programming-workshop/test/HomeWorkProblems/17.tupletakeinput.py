
## python program to create a tuple by getting input from the user ##

# write a program create a tuple by taking input from the user

mylist = []
for count in range(5):
    name=input(" Give any name : ")
    mylist.append(name)
tupletwo = (mylist[0],mylist[1],mylist[2],mylist[3],mylist[4])
print(" The elements in tuple1 are : ",tupletwo)

one = input(" Give a name : ")
two = input(" Give a name : ")
three = input(" Give a name : ")
four = input(" Give a name : ")
five = input(" Give a name : ")
tupleone = (one,two,three,four,five)
print(" The elements in tuple2 are : ",tupleone)
