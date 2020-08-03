

#Range, negative. 

#We can use range() to decrement a variable, to move downwards. We specify the 
#"step" value as the optional third parameter of range. We use -1 to decrement by one.

#Note:The second value (0) is never reached in the loop body—it is an "exclusive" boundary.

#Python program that uses range, decrements

# Loop over range with negative step.
for i in range(5, 0, -1):
    print(i)
