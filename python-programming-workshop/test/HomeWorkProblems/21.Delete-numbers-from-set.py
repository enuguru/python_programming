
# write a program which first creates a set, then takes an
# element as input and deletes that element from the set if present


newset =  {34,45,2,9,23}
print(newset)
num = 13
if num in newset:
    newset.remove(num)
print(newset)