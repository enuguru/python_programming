
'''Error in addition from input.'''

x = input("Enter a number: ")
y = input("Enter a second number: ")
print('The sum of ', x, ' and ', y, ' is ', x+y, '.', sep='') #error


# the below method is the correct way to do it
# you have to convert string in to an int

'''Two numeric inputs, with immediate conversion'''

x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))
print('The sum of ', x, ' and ', y, ' is ', x+y, '.', sep='')
