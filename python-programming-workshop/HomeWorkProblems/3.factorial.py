## python program to find the factorial of a given number  ##


max = int(input(" Give the number whose factorial you want : "))
fact = 1
for num in range(1,max+1):
    fact = fact * num
print(fact)



# write a program to print the factorial of a given
# number. can you do the factorial of the program by using list comprehension

mysum = sum(num for num in range(1,7))
print(mysum)


s = 1
p = [num for num in range(1,7)]
print(p)


#fact = lambda x: 1 if x == 0 else x * fact(x-1)
#print(fact(int(input("give your input"))))


#s = 1
#p = [s for num in range(1,5) if s.g !=0]
