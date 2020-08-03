
# write a program which first creates a set, then takes an
# element as input and deletes that element from the set if present

## python program to print unique(nonduplicate) values in a dictionary##

newset = {34,45,23,21,2,9}

number = int(input("Give a number"))

if number in newset:
    newset.discard(number)
print(newset)