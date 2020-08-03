

# Python program to ask the user for a range and display all the prime numbers in that interval

# take input from the user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
flag = 0
for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               flag = 1
               break
       if flag ==0:
           print(num)
       else:
           flag = 0
