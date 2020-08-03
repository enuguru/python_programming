

# Python program to find the sum of natural numbers up to n where n is provided by user

# take input from the user
num = int(input("Enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate un till zero
   while(num > 0):
       sum = sum + num
       num = num - 1
   print("The sum of the numbers till num is :q",sum)
