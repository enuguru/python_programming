
## python program to print numbers greater than and less than 100 
## from a given list of numbers by using list comprehension ##

# write a program to find the maximum and minimum
# value in a set

yourlist = [12, 5, 23, 79, 63, 11, 7, 6, 115, 129]

min = 10
max = 100
mincount = 0
maxcount = 0
maxlist = [i for i in yourlist if i>min]
minlist = [i for i in yourlist if i<max]
print(" Given list : ", yourlist)
print(" The numbers greater than 10 from the given list : ", maxlist)
##print(" Number of elements greater than 10 : ",maxcount) 
print(" The numbers less than 100 from the given list :  ",minlist)
##print(" Number of elements less than 100 : ",mincount)
