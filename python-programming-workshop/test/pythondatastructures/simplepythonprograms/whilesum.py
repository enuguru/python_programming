
a = 1
s = 0
print('Enter Numbers to add to the sum.')
print('Enter 0 to quit.')
while a != 0:                           
    print('Current Sum:', s)            
    a = float(input('Number? '))        
    s = s + a                            
print('Total Sum =', s)  # this print does not come in the while loop 
                         # The while statement only affects the lines that are indented 
                         # with whitespace 
