
# this is the basic method
number = int(input("Give a number"))
for val in range(2,number):
    if number % val == 0:
        print(val,end=" ")
print("\n\n")


# this is using list comprehension
factors = [val for val in range(2,number) if number % val == 0]
print(factors)


# this is using a function 
def find_factors(n):
    for val in range(2,number):
       if number % val == 0:
           print(val,end=" ")
    print("\n\n")

find_factors(number)
