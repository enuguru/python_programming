
# A python program to illustrate slicing in strings
#Note: We can also slice the string using beginning and only and steps are optional.
 
teststr = "lovelyflowersareseeninhillstationsallthetime"
 
# Prints 3rd character beginning from 0
print(teststr[2])
print(teststr[2:5])      
print(teststr[2:15:2])      
 
# Prints 7th character
print(teststr[6])  
print(teststr[4:10:2])    
 
# Prints 3rd character from rear beginning from -1
print(teststr[-3]) 
print(teststr[-7:-3]) 
print(teststr[-15:-3:2]) 
 
# Length of string is 10 so it is out of bound
print(teststr[15]) 
