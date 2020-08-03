
# Python Program to display the powers of 2 using anonymous function

# Take number of terms from user
terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

# display the result
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
