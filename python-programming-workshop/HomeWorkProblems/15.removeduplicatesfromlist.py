
## python program to remove duplicates from list ##

# Remove duplicates from a list of numbers

yourlist =  [45, 56, 45, 45, 34, 56, 67, 99]

yourlist = sorted(yourlist)
print(" Given list is : ",yourlist)

yourlist=list(set(yourlist))
print(" New list without duplicates is : ",yourlist)
